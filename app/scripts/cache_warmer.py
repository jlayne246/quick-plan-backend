# scripts/cache_warmer.py
from app.framework.cache import cache_function
from app.services.degree_service import get_degrees

def warm_degrees_cache():
    data, source = cache_function("degrees:list", get_degrees)
    print(f"Cache warmed with {len(data)} degrees (source={source})")
