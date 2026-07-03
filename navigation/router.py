# BeeRoute Router Engine (Turn-by-Turn System)
# Converts routes into human driving instructions

class Router:
    def __init__(self):
        self.step_index = 0

    def calculate_route(self, start, destination, avoid_highways=False):
        """
        Generates structured route (placeholder + navigation flow)
        """

        base_steps = [
            "Head out from current location",
            "Continue straight for a while",
            "Approach main intersection",
            "Follow road signs toward destination area",
            "Arrive at destination"
        ]

        highway_steps = [
            "Take local roads from start",
            "Avoid highway entry ramps",
            "Continue through city streets",
            "Stay on alternate route",
            "Approach destination",
            "Arrive at destination"
        ]

        route = {
            "start": start,
            "destination": destination,
            "steps": highway_steps if avoid_highways else base_steps,
            "current_step": 0,
            "total_steps": len(highway_steps if avoid_highways else base_steps),
            "mode": "avoid_highways" if avoid_highways else "normal"
        }

        return route

    def get_next_instruction(self, route):
        """
        Returns next turn-by-turn instruction
        """

        steps = route.get("steps", [])
        index = route.get("current_step", 0)

        if index >= len(steps):
            return "You have arrived at your destination."

        instruction = steps[index]

        route["current_step"] += 1

        return instruction
