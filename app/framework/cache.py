import json
from app.utilities.redis_client import cache

def cache_function(key, func, ttl=3600):
    """
    Wrap a function call with caching in Redis.
    """
    # Check cache
    cached_value = cache.get(key)
    if cached_value:
        return json.loads(cached_value), "cache"

    # Cache miss → call the original function
    result = func()

    # Save to cache
    cache.setex(key, ttl, json.dumps(result))
    return result, "database"