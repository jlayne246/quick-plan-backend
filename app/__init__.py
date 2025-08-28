from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    # Config
    app.config.from_object("app.config.Config")

    # Enable CORS so Next.js frontend can talk to backend
    CORS(app)
    
    # Simple hello world route
    @app.route("/api/hello")
    def hello():
        return {"message": "Hello, World!"}

    # Register blueprints (API routes)
    # from app.routes.courses import courses_bp
    # app.register_blueprint(courses_bp, url_prefix="/api/courses")

    return app
