# BeeRoute Navigation Router (basic path engine)

class Router:
    def __init__(self):
        self.mode = "fastest"

    def set_mode(self, mode):
        self.mode = mode

    def calculate_route(self, start, destination):
        return {
            "start": start,
            "destination": destination,
            "mode": self.mode,
            "route": [
                "Step 1: Start navigation",
                "Step 2: Follow main road",
                "Step 3: Continue straight",
                "Step 4: Arrive at destination"
            ]
        }


if __name__ == "__main__":
    r = Router()
    print(r.calculate_route("A", "B"))
