import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bus_utils import search_routes, get_bus_location, calculate_fare, format_bus_status

def test_search_returns_results():
    results = search_routes("Divisoria")
    assert len(results) > 0

def test_search_empty_query_returns_empty():
    results = search_routes("")
    assert results == []

def test_bus_location_has_required_fields():
    location = get_bus_location(1)
    assert "lat" in location
    assert "lng" in location

def test_fare_minimum_distance():
    fare = calculate_fare(2)
    assert fare >= 13

def test_fare_scales_with_distance():
    assert calculate_fare(10) > calculate_fare(3)