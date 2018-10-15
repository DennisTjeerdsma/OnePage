from flask import Flask
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    #App setup
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.debug = True

    # Initializing app
    db.init_app(app)
    migrate.init_app(app, db)

    #Registring blueprints
    from app.main import routes_bp
    app.register_blueprint(routes_bp)

    #Initializing CORS
    CORS(app, support_crendentials=True)

    return app