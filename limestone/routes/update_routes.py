from flask import Blueprint, request, jsonify, session, current_app
from ..database import get_db
from datetime import datetime
import json

update_bp = Blueprint("update", __name__)

@update_bp.route("/update", methods=["POST"])
def update_data():
    api_key = request.headers.get("Authorization", "")
    if api_key != f"Bearer {current_app.config['DASHBOARD_API_KEY']}":
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    node = data.get("node")
    status = data.get("status")
    rock_stats = data.get("rock_stats")

    conn = get_db()
    cur = conn.cursor()

    for size_range, count in rock_stats.items():
        cur.execute(
            "INSERT INTO realdata (node, status, size_range, count, timestamp) VALUES (%s, %s, %s, %s, %s)",
            (node, status, size_range, count, datetime.utcnow())
        )

    cur.execute("UPDATE meta SET value = %s WHERE key = 'last_update'", (datetime.utcnow().isoformat(),))
    conn.commit()
    cur.close()

    return jsonify({"message": "Data updated successfully"})

@update_bp.route("/reset", methods=["POST"])
def reset_data():
    if not session.get("logged_in"):
        return jsonify({"error": "Not logged in"}), 403

    reset_key = request.headers.get("Authorization", "")
    if reset_key != f"Bearer {current_app.config['RESET_KEY']}":
        return jsonify({"error": "Unauthorized"}), 403

    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM realdata;")
    cur.execute("UPDATE meta SET value = %s WHERE key = 'last_update'", (datetime.utcnow().isoformat(),))
    conn.commit()
    cur.close()

    return jsonify({"message": "All data cleared"})
