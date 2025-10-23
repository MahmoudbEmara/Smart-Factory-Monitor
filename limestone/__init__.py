from flask import Flask
from .database import init_db
from .routes.auth_routes import auth_bp
from .routes.update_routes import update_bp
from .routes.dashboard_routes import dashboard_bp
from .routes.dailytrend_routes import dailytrend_bp
from .routes.history_routes import history_bp
import os

def create_app():
    # Tell Flask where to find templates and static files
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), "templates"),
        static_folder=os.path.join(os.path.dirname(__file__), "static")
    )

    app.config.from_object("config.Config")

    # Initialize DB
    init_db(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(update_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(dailytrend_bp)
    app.register_blueprint(history_bp)

    return app
