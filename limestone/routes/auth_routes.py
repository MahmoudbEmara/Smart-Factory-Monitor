from flask import Blueprint, render_template, request, redirect, session, url_for, current_app

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("password")

        if user == current_app.config["LOGIN_USER"] and password == current_app.config["LOGIN_PASS"]:
            session["logged_in"] = True
            return redirect(url_for("dashboard.dashboard"))
        else:
            return render_template("index.html", error="Invalid credentials")

    return render_template("index.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
