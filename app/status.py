# status.py
from flask import Blueprint, jsonify
from sqlalchemy import create_engine, text
import redis
import requests
import psutil
import time
import os
from datetime import datetime
from dotenv import load_dotenv

# Create a Blueprint for modular import
status_bp = Blueprint("status", __name__)

load_dotenv()

# --- Configuration ---
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
EXTERNAL_API = os.getenv("EXTERNAL_API", "https://api.github.com")

# --- Connections ---
db_engine = create_engine(DATABASE_URL)
cache = redis.from_url(REDIS_URL, decode_responses=True)

start_time = time.time()

# --- Health check helpers ---
def check_database():
    try:
        with db_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok", "message": "Database connected"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def check_cache():
    try:
        cache.ping()
        return {"status": "ok", "message": "Redis connected"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def check_external_api():
    try:
        resp = requests.get(EXTERNAL_API, timeout=3)
        if resp.status_code == 200:
            return {"status": "ok", "message": f"External API reachable ({EXTERNAL_API})"}
        else:
            return {"status": "error", "message": f"Unexpected status {resp.status_code}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- Route definitions ---
@status_bp.route("/status")
def status():
    uptime = round(time.time() - start_time, 2)
    db = check_database()
    cache_status = check_cache()
    external = check_external_api()

    process = psutil.Process(os.getpid())
    memory = process.memory_info().rss / 1024 / 1024
    cpu = psutil.cpu_percent(interval=0.1)

    overall_ok = all(s["status"] == "ok" for s in [db, cache_status,external])

    response = {
        "status": "ok" if overall_ok else "degraded",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "uptime_seconds": uptime,
        "system": {"cpu_percent": cpu, "memory_mb": round(memory, 2)},
        "services": {
            "database": db,
            "cache": cache_status,
            "external_api": external,
        },
    }

    return jsonify(response), (200 if overall_ok else 503)
