# BusTrack - Bus Utility Functions
# Secured + Logged: input validation, token auth, named constants, logging

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("bustrack.log")
    ]
)
logger = logging.getLogger(__name__)

ROUTES = [
    {"id": 1, "name": "Divisoria to SM City", "stops": 12},
    {"id": 2, "name": "Cogon to Limketkai", "stops": 8},
    {"id": 3, "name": "Bulua to Downtown", "stops": 10},
]

BUS_LOCATIONS = {
    1: {"lat": 8.4542, "lng": 124.6319},
    2: {"lat": 8.4700, "lng": 124.6400},
}

BASE_FARE = 13
FARE_PER_KM = 1.8
MIN_DISTANCE_KM = 4
MAX_QUERY_LENGTH = 100

VALID_TOKENS = {"bustrack-admin-token-2026"}

def authenticate(token):
    if not token or not isinstance(token, str):
        logger.warning("Authentication attempted with empty or invalid token")
        return False
    result = token in VALID_TOKENS
    logger.info(f"Authentication attempt -> {'success' if result else 'failed'}")
    return result

def search_routes(query):
    if not query or not isinstance(query, str):
        logger.warning("search_routes called with empty or invalid query")
        return []
    query = query.strip()
    if len(query) > MAX_QUERY_LENGTH:
        logger.error(f"Query too long: {len(query)} chars")
        raise ValueError(f"Query too long. Max {MAX_QUERY_LENGTH} characters.")
    if not query.replace(" ", "").isalnum():
        logger.error(f"Query contains invalid characters: {query}")
        raise ValueError("Query contains invalid characters.")
    results = [r for r in ROUTES if query.lower() in r["name"].lower()]
    logger.info(f"search_routes('{query}') returned {len(results)} result(s)")
    return results

def get_bus_location(bus_id):
    if not isinstance(bus_id, int) or bus_id <= 0:
        logger.error(f"Invalid bus_id received: {bus_id}")
        raise ValueError("bus_id must be a positive integer.")
    result = BUS_LOCATIONS.get(bus_id, {"status": "unavailable"})
    logger.info(f"get_bus_location({bus_id}) -> {result}")
    return result

def calculate_fare(distance_km):
    if distance_km <= MIN_DISTANCE_KM:
        return BASE_FARE
    return BASE_FARE + (distance_km - MIN_DISTANCE_KM) * FARE_PER_KM

def format_bus_status(bus_id):
    loc = get_bus_location(bus_id)
    if "status" in loc:
        return "unavailable"
    return "active"