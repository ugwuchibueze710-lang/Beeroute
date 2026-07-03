# BeeRoute Router Engine (A* Pathfinding Core)
# Real shortest-path navigation logic

import heapq
import math


class Router:
    def __init__(self):
        self.graph = {}

    # ----------------------------
    # GRAPH BUILDING
    # ----------------------------
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, from_node, to_node, distance):
        self.add_node(from_node)
        self.add_node(to_node)

        self.graph[from_node].append((to_node, distance))
        self.graph[to_node].append((from_node, distance))  # undirected road

    # ----------------------------
    # HEURISTIC (A*)
    # ----------------------------
    def heuristic(self, a, b):
        # simple straight-line estimate if coordinates exist
        if isinstance(a, tuple) and isinstance(b, tuple):
            return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

        return 1  # fallback

    # ----------------------------
    # A* PATHFINDING
    # ----------------------------
    def find_path(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))

        came_from = {}
        g_score = {node: float("inf") for node in self.graph}
        g_score[start] = 0

        f_score = {node: float("inf") for node in self.graph}
        f_score[start] = self.heuristic(start, goal)

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor, cost in self.graph.get(current, []):
                tentative_g = g_score[current] + cost

                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, goal)

                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return []

    # ----------------------------
    # REBUILD PATH
    # ----------------------------
    def reconstruct_path(self, came_from, current):
        path = [current]

        while current in came_from:
            current = came_from[current]
            path.append(current)

        path.reverse()
        return path

    # ----------------------------
    # PUBLIC ROUTE FUNCTION
    # ----------------------------
    def calculate_route(self, start, destination, avoid_highways=False):
        path = self.find_path(start, destination)

        if not path:
            return {
                "start": start,
                "destination": destination,
                "steps": ["No route found"],
                "graph_ready": True
            }

        steps = []
        for i in range(len(path) - 1):
            steps.append(f"Go from {path[i]} to {path[i+1]}")

        return {
            "start": start,
            "destination": destination,
            "path": path,
            "steps": steps,
            "graph_ready": True
        }

    # ----------------------------
    # TURN-BY-TURN
    # ----------------------------
    def get_next_instruction(self, route):
        if "current_step" not in route:
            route["current_step"] = 0

        steps = route.get("steps", [])
        i = route["current_step"]

        if i >= len(steps):
            return "You have arrived at your destination."

        instruction = steps[i]
        route["current_step"] += 1

        return instruction
