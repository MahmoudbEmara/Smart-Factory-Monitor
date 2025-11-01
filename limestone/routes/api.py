from flask import Blueprint, jsonify, request, session, redirect, current_app
from datetime import datetime, timedelta, timezone
from dateutil import parser
from collections import defaultdict
import hashlib, json, re

from limestone.utils import get_db_conn, RESET_KEY, EGYPT_TZ

api_bp = Blueprint('api', __name__)

# ---------------- Dashboard Data ----------------
@api_bp.route('/dashboard-data')
def dashboard_data():
    if not session.get("logged_in"):
        return jsonify({"error": "Unauthorized"}), 403

    try:
        with get_db_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT node, size_range, SUM(count)
                    FROM realdata
                    GROUP BY node, size_range
                    ORDER BY node;
                """)
                rows = cur.fetchall()

                cur.execute("SELECT MAX(timestamp) FROM realdata;")
                last_updated = cur.fetchone()[0]

        if last_updated:
            last_updated = last_updated.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
        else:
            last_updated = "No data yet"

        result = {"totals": {}, "last_updated": last_updated}

        for node, size_range, count in rows:
            if node not in result["totals"]:
                result["totals"][node] = {}
            result["totals"][node][size_range] = count

        return jsonify(result)

    except Exception as e:
        print("Error in /dashboard-data:", e)
        return jsonify({"error": "Internal Server Error"}), 500

# ---------------- Reset Database ----------------
@api_bp.route('/reset', methods=['POST'])
def reset():
    if not session.get('logged_in'):
        return redirect('/')

    if request.headers.get("Authorization", "") != f"Bearer {RESET_KEY}":
        return jsonify({"error": "Unauthorized"}), 401

    with get_db_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM realdata")
            cur.execute("DELETE FROM meta WHERE key='last_update'")
            conn.commit()

    return jsonify({"message": "Dashboard data reset."})

# ---------------- History Trend (Past 7 Days) ----------------
@api_bp.route('/api/history')
def api_history():
    if not session.get("logged_in"):
        return jsonify({"error": "Unauthorized"}), 403

    today = datetime.now(EGYPT_TZ).date()
    start_day = today - timedelta(days=6)

    categories = ["<30mm", "30-50mm", "50-80mm", "80-150mm", ">150mm"]

    # Initialize structure for full 7 days
    day_data = {
        start_day + timedelta(days=i): {cat: 0 for cat in categories}
        for i in range(7)
    }

    try:
        with get_db_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT
                        DATE(timestamp AT TIME ZONE 'Africa/Cairo') AS day,
                        size_range,
                        SUM(count)
                    FROM realdata
                    WHERE DATE(timestamp AT TIME ZONE 'Africa/Cairo') >= %s
                    GROUP BY 1, size_range
                    ORDER BY 1;
                """, (start_day,))
                rows = cur.fetchall()

                # Get last updated timestamp
                cur.execute("SELECT value FROM meta WHERE key='last_update'")
                row = cur.fetchone()
                last_updated = row[0] if row else "No recent data"

        def normalize(sr):
            sr = sr.lower().replace(" ", "")
            if sr.startswith("<30"): return "<30mm"
            if sr.startswith("30") or sr.startswith("30-50"): return "30-50mm"
            if sr.startswith("50") or sr.startswith("50-80"): return "50-80mm"
            if sr.startswith("80") or sr.startswith("80-150"): return "80-150mm"
            if sr.startswith(">") or sr.startswith(">150"): return ">150mm"
            return None

        # Populate counts
        for day, sr, total in rows:
            cat = normalize(sr)
            if cat and day in day_data:
                day_data[day][cat] += total

        # Build response data
        dates = []
        percents = {cat: [] for cat in categories}

        for day in sorted(day_data.keys()):
            totals = day_data[day]
            total_sum = sum(totals.values())
            dates.append(day.strftime("%d/%m/%y"))

            for cat in categories:
                pct = (totals[cat] / total_sum * 100) if total_sum else 0
                percents[cat].append(round(pct, 2))

        return jsonify({
            "dates": dates,
            "last_updated": last_updated,
            **percents
        })

    except Exception as e:
        print("Error in /api/history:", e)
        return jsonify({"error": "Internal Server Error"}), 500

# ---------------- Daily Trend ----------------
@api_bp.route('/api/daily-trend')
def api_daily_trend():
    if not session.get("logged_in"):
        return jsonify({"error": "Unauthorized"}), 403

    try:
        with get_db_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT value FROM meta WHERE key='last_update'")
                row = cur.fetchone()
                end_time = parser.isoparse(row[0]) if row else datetime.now(timezone.utc)

        end_time = end_time.astimezone(timezone.utc)
        start_time = end_time - timedelta(hours=24)

        categories = ['<30mm', '30-50mm', '50-80mm', '80-150mm', '>150mm']
        color_map = {
            '<30mm': '#1f77b4', '30-50mm': '#ff7f0e', '50-80mm': '#2ca02c',
            '80-150mm': '#d62728', '>150mm': '#9467bd',
        }

        with get_db_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT 
                        DATE_TRUNC('minute', timestamp AT TIME ZONE 'UTC'),
                        size_range,
                        SUM(count)
                    FROM realdata
                    WHERE timestamp >= %s AND timestamp < %s
                    GROUP BY 1, size_range
                    ORDER BY 1;
                """, (start_time, end_time))
                rows = cur.fetchall()

        minute_bins = defaultdict(lambda: defaultdict(int))
        for minute, sr, total in rows:
            minute_str = minute.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")
            minute_bins[minute_str][sr] += total

        sorted_times = sorted(minute_bins.keys())

        datasets = []
        for cat in categories:
            vals = []
            for t in sorted_times:
                total = sum(minute_bins[t].values())
                pct = (minute_bins[t][cat] / total * 100) if total else 0
                vals.append(round(pct, 2))
            datasets.append({
                "label": cat,
                "values": vals,
                "color": color_map[cat]
            })

        payload = {
            "timestamps": sorted_times,
            "datasets": datasets,
            "last_updated": end_time.isoformat().replace("+00:00", "Z")
        }

        data_hash = hashlib.md5(json.dumps(payload, sort_keys=True).encode()).hexdigest()
        payload["data_hash"] = data_hash

        return jsonify(payload)

    except Exception as e:
        print("Error in /api/daily-trend:", e)
        return jsonify({"error": "Internal Server Error"}), 500
