from flask import Flask
from .database import init_db
import os

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), "templates"),
        static_folder=os.path.join(os.path.dirname(__file__), "static")
    )

    app.config.from_object("config.Config")

    init_db(app)

    from .routes.auth_routes import auth_bp
    from .routes.update_routes import update_bp
    from .routes.dashboard_routes import dashboard_bp testing
    from .routes.dailytrend_routes import dailytrend_bp
    from .routes.history_routes import history_bp
    from .routes.api import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(update_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(dailytrend_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(api_bp)

    return app
