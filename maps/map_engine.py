# BeeRoute Map Engine (OpenStreetMap Data Layer Foundation)
# This prepares real map data ingestion for routing later

import math


class MapEngine:
    def __init__(self):
        self.current_location = None
        self.osm_data = {
            "nodes": {},
            "roads": []
        }

    def set_location(self, lat, lon):
        """
        Store GPS coordinates
        """
        self.current_location = (lat, lon)
        return f"Location set to {lat}, {lon}"

    def get_location(self):
        return self.current_location

    def load_osm_placeholder(self, area_name="default"):
        """
        Placeholder for OpenStreetMap data loading
        (real version will fetch road graph data later)
        """

        self.osm_data = {
            "area": area_name,
            "nodes": {
                "A": (0, 0),
                "B": (1, 1),
                "C": (2, 2)
            },
            "roads": [
                ("A", "B"),
                ("B", "C")
            ]
        }

        return f"OSM data loaded for {area_name}"

    def haversine_distance(self, coord1, coord2):
        """
        Real-world distance calculation (km)
        """
        R = 6371

        lat1, lon1 = coord1
        lat2, lon2 = coord2

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)

        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c

    def estimate_distance(self, start, end):
        """
        Distance wrapper for routing system
        """

        if isinstance(start, tuple) and isinstance(end, tuple):
            return self.haversine_distance(start, end)

        return "Invalid coordinates"
