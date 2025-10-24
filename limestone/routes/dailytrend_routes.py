from flask import Blueprint, render_template, jsonify, session, redirect, url_for
from limestone.utils import get_db_conn

dailytrend_bp = Blueprint("dailytrend", __name__)

@dailytrend_bp.route("/dailytrend")
def dailytrend_page():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("dailytrend.html")
