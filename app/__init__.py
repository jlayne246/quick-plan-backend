from flask import Flask
from flask_cors import CORS

import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from sqlalchemy import text

from app.extensions import db

from app.routes.semester_routes import semester_bp

def create_app():
    load_dotenv()  # Load environment variables from .env file
    
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    
    # ✅ Test DB connection on startup
    with app.app_context():
        try:
            db.session.execute(text("SELECT 1"))  # simple query
            print("✅ Database connection successful")
        except Exception as e:
            print("❌ Database connection failed:", e)
    
    # Config
    app.config.from_object("app.config.Config")

    # Enable CORS so Next.js frontend can talk to backend
    CORS(app)
    
    # Simple hello world route
    @app.route("/api/hello")
    def hello():
        return {"message": "Hello, World!"}

    # Register blueprints (API routes)
    # Register blueprints
    app.register_blueprint(semester_bp, url_prefix="/api")
    
    return app
