import re
import time
from uuid import uuid4
from .config import HEADERS, CACHE_TTL


CACHE = {}




def new_id(prefix="id"):
return f"{prefix}_{uuid4().hex[:8]}"




def sanitize_interests(interests):
if not interests:
return []
if isinstance(interests, str):
return [s.strip().lower() for s in re.split(r"[,\|/;]+", interests) if s.strip()]
return [str(x).strip().lower() for x in interests if str(x).strip()]




def get_cache(key, ttl=CACHE_TTL):
v = CACHE.get(key)
if v is None:
return None
ts, data = v
if time.time() - ts > ttl:
CACHE.pop(key, None)
return None
return data




def set_cache(key, data):
CACHE[key] = (time.time(), data)