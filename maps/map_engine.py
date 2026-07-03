# BeeRoute Map Engine (OpenStreetMap Real Data Layer)
# Connects real-world map data to routing engine

import osmnx as ox


class MapEngine:
    def __init__(self):
        self.graph = None
        self.current_location = None

    # ----------------------------
    # LOAD REAL MAP DATA
    # ----------------------------
    def load_city(self, place_name):
        """
        Downloads real road network from OpenStreetMap
        """
        print(f"Loading map for {place_name}...")

        self.graph = ox.graph_from_place(
            place_name,
            network_type="drive"
        )

        return f"Map loaded for {place_name}"

    # ----------------------------
    # SET LOCATION
    # ----------------------------
    def set_location(self, lat, lon):
        self.current_location = (lat, lon)
        return self.current_location

    # ----------------------------
    # FIND NEAREST NODE
    # ----------------------------
    def get_nearest_node(self, lat, lon):
        if self.graph is None:
            return None

        return ox.distance.nearest_nodes(
            self.graph,
            lon,
            lat
        )

    # ----------------------------
    # GET ROUTE (REAL ROAD PATH)
    # ----------------------------
    def get_route(self, start_lat, start_lon, end_lat, end_lon):
        if self.graph is None:
            return None

        start_node = self.get_nearest_node(start_lat, start_lon)
        end_node = self.get_nearest_node(end_lat, end_lon)

        route = ox.shortest_path(
            self.graph,
            start_node,
            end_node,
            weight="length"
        )

        return route
