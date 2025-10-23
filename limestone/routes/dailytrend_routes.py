from flask import Blueprint, render_template, jsonify, session, redirect, url_for
from ..database import get_db

dailytrend_bp = Blueprint("dailytrend", __name__)

@dailytrend_bp.route("/dailytrend")
def dailytrend_page():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("dailytrend.html")

@dailytrend_bp.route("/api/daily-trend")
def dailytrend_data():
    if not session.get("logged_in"):
        return jsonify({"error": "Unauthorized"}), 403

    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT size_range, date_trunc('minute', timestamp) AS minute, SUM(count)
        FROM realdata
        WHERE timestamp >= NOW() - INTERVAL '24 hours'
        GROUP BY size_range, minute
        ORDER BY minute;
    """)
    rows = cur.fetchall()
    cur.close()

    data = {}
    for size, minute, count in rows:
        data.setdefault(size, []).append({"minute": minute.isoformat(), "count": count})

    return jsonify(data)
