from flask import Flask
from flask_cors import CORS

import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from sqlalchemy import text

from app.status import status_bp  # import your modular status routes

from app.extensions import db

from app.routes.semester_routes import semester_bp
from app.routes.degree_routes import degree_bp
from app.routes.faculty_routes import faculty_bp

def create_app():
    load_dotenv()  # Load environment variables from .env file
    
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    app.register_blueprint(status_bp)  # registers /status route
    app.register_blueprint(semester_bp, url_prefix="/api")
    app.register_blueprint(degree_bp, url_prefix="/api")
    app.register_blueprint(faculty_bp, url_prefix="/api")
    
    # print("DB URI in config:", app.config.get("SQLALCHEMY_DATABASE_URI"))
    
    db.init_app(app)
    
    with app.app_context():
        from app.framework.cache_warmer import warm_degrees_cache
        warm_degrees_cache()
    
    # ✅ Test DB connection on startup
    with app.app_context():
        try:
            db.session.execute(text("SELECT 1"))  # simple query
            print("✅ Database connection successful")
        except Exception as e:
            print("❌ Database connection failed:", e)
    
    # Config
    #app.config.from_object("app.config.Config")
    

    # Enable CORS so Next.js frontend can talk to backend
    CORS(app)
    
    # Simple hello world route
    @app.route("/api/hello")
    def hello():
        return {"message": "Hello, World!"}
    
    @app.route("/")
    def home():
        return """
                <html>
                <head><title>Service Status</title></head>
                <body style="font-family:sans-serif; text-align:center; padding-top:3em;">
                    <h1>✅ Flask Backend Running</h1>
                    <p>See <a href='/status'>/status</a> for full system report.</p>
                </body>
                </html>
            """

    # Register blueprints (API routes)
    # Register blueprints
    

    return app
