from flask import Flask
from config import Config
from flask_cors import CORS

def create_app(config_class=Config):
    #App setup
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.debug = True

    #Registring blueprints
    from app.main import routes_bp
    app.register_blueprint(routes_bp)

    #Initializing CORS
    CORS(app)

    
    return app