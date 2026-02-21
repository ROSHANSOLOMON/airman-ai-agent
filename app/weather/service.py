from datetime import datetime

# simple in-memory cache
weather_cache = {}


def get_weather(icao, start_time, end_time):

    key = f"{icao}-{start_time}-{end_time}"

    # cache hit
    if key in weather_cache:
        return weather_cache[key]

    try:
        # simulated weather (for now)
        weather = {
            "ceiling": 1000,
            "visibility": 5,
            "wind": 10,
            "fetched_at": str(datetime.utcnow())
        }

        weather_cache[key] = weather
        return weather

    except Exception:
        # deterministic fallback
        return None