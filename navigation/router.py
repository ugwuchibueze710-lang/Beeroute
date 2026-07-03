import heapq
import math


class Router:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, a, b, distance):
        self.add_node(a)
        self.add_node(b)

        self.graph[a].append((b, distance))
        self.graph[b].append((a, distance))

    def heuristic(self, a, b):
        return 1

    def find_path(self, start, goal):
        open_set = [(0, start)]
        came_from = {}

        g = {start: 0}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return self.reconstruct(came_from, current)

            for neighbor, cost in self.graph.get(current, []):
                new_cost = g[current] + cost

                if neighbor not in g or new_cost < g[neighbor]:
                    g[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (priority, neighbor))
                    came_from[neighbor] = current

        return []

    def reconstruct(self, came_from, current):
        path = [current]

        while current in came_from:
            current = came_from[current]
            path.append(current)

        return list(reversed(path))

    def calculate_route(self, start, destination):
        path = self.find_path(start, destination)

        if not path:
            return {"steps": ["No route found"]}

        steps = []
        for i in range(len(path) - 1):
            steps.append(f"Go from {path[i]} to {path[i+1]}")

        return {
            "path": path,
            "steps": steps
        }

    def get_next_instruction(self, route):
        if "index" not in route:
            route["index"] = 0

        i = route["index"]
        steps = route.get("steps", [])

        if i >= len(steps):
            return "You have arrived at your destination."

        route["index"] += 1
        return steps[i]
