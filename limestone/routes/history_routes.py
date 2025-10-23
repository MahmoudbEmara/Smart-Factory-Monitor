from flask import Blueprint, render_template, jsonify, session, redirect, url_for
from ..database import get_db

history_bp = Blueprint("history", __name__)

@history_bp.route("/history")
def history_page():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("history.html")

@history_bp.route("/api/history")
def history_data():
    if not session.get("logged_in"):
        return jsonify({"error": "Unauthorized"}), 403

    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT size_range, date_trunc('day', timestamp) AS day, SUM(count)
        FROM realdata
        WHERE timestamp >= NOW() - INTERVAL '7 days'
        GROUP BY size_range, day
        ORDER BY day;
    """)
    rows = cur.fetchall()
    cur.close()

    data = {}
    for size, day, count in rows:
        data.setdefault(size, []).append({"day": day.isoformat(), "count": count})

    return jsonify(data)
