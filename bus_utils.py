ROUTES = [
    {"id": 1, "name": "Divisoria to SM City", "stops": 12},
    {"id": 2, "name": "Cogon to Limketkai", "stops": 8},
    {"id": 3, "name": "Bulua to Downtown", "stops": 10},
]

BUS_LOCATIONS = {
    1: {"lat": 8.4542, "lng": 124.6319},
    2: {"lat": 8.4700, "lng": 124.6400},
}

def search_routes(query):
    if not query:
        return []
    return [r for r in ROUTES if query.lower() in r["name"].lower()]

def get_bus_location(bus_id):
    return BUS_LOCATIONS.get(bus_id, {"status": "unavailable"})

def calculate_fare(distance_km):
    base = 13
    if distance_km <= 4:
        return base
    return base + (distance_km - 4) * 1.8

def format_bus_status(bus_id):
    loc = get_bus_location(bus_id)
    if "status" in loc:
        return "unavailable"
    return "active"