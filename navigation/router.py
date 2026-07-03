# BeeRoute Router Engine (Graph-Based Foundation)
# Prepares system for OpenStreetMap road graph routing

class Router:
    def __init__(self):
        # simple graph structure placeholder
        self.graph = {}

    def add_node(self, node):
        """
        Add a road intersection / point
        """
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, from_node, to_node, distance=1):
        """
        Connect two road points
        """
        self.add_node(from_node)
        self.add_node(to_node)

        self.graph[from_node].append({
            "to": to_node,
            "distance": distance
        })

    def calculate_route(self, start, destination, avoid_highways=False):
        """
        Placeholder route builder (future: Dijkstra/A*)
        """

        route = {
            "start": start,
            "destination": destination,
            "mode": "avoid_highways" if avoid_highways else "normal",
            "graph_ready": True,
            "steps": []
        }

        # simple fake traversal (graph-ready structure)
        route["steps"] = [
            f"Start at {start}",
            "Enter road network",
            "Navigate through intersections",
            f"Approach {destination}",
            "Arrive at destination"
        ]

        if avoid_highways:
            route["steps"].insert(2, "Avoid highway nodes and use local roads only")

        return route

    def get_next_instruction(self, route):
        """
        Turn-by-turn placeholder (graph-ready upgrade point)
        """

        if "current_step" not in route:
            route["current_step"] = 0

        steps = route.get("steps", [])
        i = route["current_step"]

        if i >= len(steps):
            return "You have arrived at your destination."

        instruction = steps[i]
        route["current_step"] += 1

        return instruction
