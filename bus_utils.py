# BusTrack - Bus Utility Functions
# Refactored + Secured: input validation, auth token check, named constants

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

# Simple token-based authentication
VALID_TOKENS = {"bustrack-admin-token-2026"}

def authenticate(token):
    """Basic token authentication. Returns True if token is valid."""
    if not token or not isinstance(token, str):
        return False
    return token in VALID_TOKENS

# --- Input Validation (Security: Place 1) ---
def search_routes(query):
    """Search routes by name. Validates input before processing."""
    if not query or not isinstance(query, str):
        return []
    query = query.strip()
    if len(query) > MAX_QUERY_LENGTH:
        raise ValueError(f"Query too long. Max {MAX_QUERY_LENGTH} characters.")
    if not query.replace(" ", "").isalnum():
        raise ValueError("Query contains invalid characters.")
    return [r for r in ROUTES if query.lower() in r["name"].lower()]

# --- Input Validation (Security: Place 2) ---
def get_bus_location(bus_id):
    """Get bus location by ID. Validates bus_id is a positive integer."""
    if not isinstance(bus_id, int) or bus_id <= 0:
        raise ValueError("bus_id must be a positive integer.")
    return BUS_LOCATIONS.get(bus_id, {"status": "unavailable"})

def calculate_fare(distance_km):
    if distance_km <= MIN_DISTANCE_KM:
        return BASE_FARE
    return BASE_FARE + (distance_km - MIN_DISTANCE_KM) * FARE_PER_KM

def format_bus_status(bus_id):
    loc = get_bus_location(bus_id)
    if "status" in loc:
        return "unavailable"
    return "active"