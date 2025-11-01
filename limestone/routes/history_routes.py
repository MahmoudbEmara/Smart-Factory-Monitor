from flask import Blueprint, render_template, jsonify, session, redirect, url_for

history_bp = Blueprint("history", __name__)

@history_bp.route("/history")
def history_page():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("history.html")
