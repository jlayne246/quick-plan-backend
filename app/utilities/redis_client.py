# redis_client.py
import redis
import os

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
cache = redis.from_url(redis_url, decode_responses=True)
