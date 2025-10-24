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
                # Query totals per size per node
                cur.execute("""
                    SELECT node, size_range, SUM(count)
                    FROM realdata
                    GROUP BY node, size_range
                    ORDER BY node;
                """)
                rows = cur.fetchall()

                # Query latest timestamp
                cur.execute("SELECT MAX(timestamp) FROM realdata;")
                last_updated = cur.fetchone()[0]

        # Build results structure
        result = {
            "totals": {},
            "last_updated": last_updated if last_updated else "No data yet"
        }

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


# ---------------- History Trend ----------------
@api_bp.route('/api/history')
def api_history():
    today = datetime.now(tz=EGYPT_TZ).date()
    seven_days_ago = today - timedelta(days=6)

    def classify_range(size_range_str):
        nums = [int(n) for n in re.findall(r'\d+', size_range_str)]
        if not nums:
            return None

        if len(nums) == 1:
            val = nums[0]
            if "<" in size_range_str:
                return "<30mm" if val == 30 else None
            if ">" in size_range_str:
                return ">150mm" if val == 150 else None
            return None

        low, high = nums
        if high <= 30: return "<30mm"
        if high <= 50: return "30-50mm"
        if high <= 80: return "50-80mm"
        if high <= 150: return "80-150mm"
        return ">150mm"

    with get_db_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    DATE(timestamp AT TIME ZONE 'Africa/Cairo'),
                    size_range,
                    SUM(count)
                FROM realdata
                WHERE DATE(timestamp AT TIME ZONE 'Africa/Cairo') >= %s
                GROUP BY 1, size_range
                ORDER BY 1;
            """, (seven_days_ago,))
            rows = cur.fetchall()

            cur.execute("SELECT value FROM meta WHERE key='last_update'")
            row = cur.fetchone()
            last_updated = row[0] if row else None

    categories = ["<30mm", "30-50mm", "50-80mm", "80-150mm", ">150mm"]
    day_data = {
        seven_days_ago + timedelta(days=i): {cat: 0 for cat in categories}
        for i in range(7)
    }

    for day, sr, total in rows:
        sr_clean = sr.lower().replace(" ", "")
        cat = classify_range(sr_clean)
        if cat and day in day_data:
            day_data[day][cat] += total

    dates = []
    percents = {cat: [] for cat in categories}

    for day in sorted(day_data.keys()):
        totals = day_data[day]
        total_count = sum(totals.values())
        dates.append(day.strftime("%d/%m/%y"))

        for cat in categories:
            pct = (totals[cat] / total_count * 100) if total_count else 0
            percents[cat].append(round(pct, 2))

    return jsonify({
        "dates": dates,
        "last_updated": last_updated,
        **percents
    })


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
            minute_str = minute.replace(tzinfo=timezone.utc).isoformat()
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
            "last_updated": end_time.isoformat()
        }

        data_hash = hashlib.md5(json.dumps(payload, sort_keys=True).encode()).hexdigest()
        payload["data_hash"] = data_hash

        return jsonify(payload)

    except Exception as e:
        print("Error in /api/daily-trend:", e)
        return jsonify({"error": "Internal Server Error"}), 500
