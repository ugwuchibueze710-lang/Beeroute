# BeeRoute Router Engine (Foundation Version)
# Builds structured routes for future real GPS integration

class Router:
    def __init__(self):
        pass

    def calculate_route(self, start, destination, avoid_highways=False):
        """
        Returns a structured route plan (placeholder for real map engine later)
        """

        route = {
            "start": start,
            "destination": destination,
            "steps": [
                "Start navigation",
                "Follow main road",
                "Continue straight for a while",
                "Approaching destination area",
                "Arrive at destination"
            ],
            "distance": "calculated later with map engine",
            "eta": "calculated later with traffic engine",
            "mode": "default"
        }

        if avoid_highways:
            route["mode"] = "avoid_highways"
            route["steps"] = [
                "Start navigation",
                "Take local roads",
                "Avoid highways as requested",
                "Follow backroads and city streets",
                "Approaching destination",
                "Arrive at destination"
            ]

        return route
