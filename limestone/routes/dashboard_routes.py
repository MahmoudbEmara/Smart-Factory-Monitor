from flask import Blueprint, render_template, jsonify, session, redirect, url_for
from ..database import get_db

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("dashboard.html")

    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT node, size_range, SUM(count)
        FROM realdata
        GROUP BY node, size_range
        ORDER BY node;
    """)
    data = cur.fetchall()
    cur.close()

    results = {}
    for node, size, count in data:
        results.setdefault(node, {})[size] = count

    return jsonify(results)
