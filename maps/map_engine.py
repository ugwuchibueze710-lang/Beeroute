class MapEngine:
    def __init__(self):
        self.location = None

    def set_location(self, lat, lon):
        self.location = (lat, lon)
        return self.location
