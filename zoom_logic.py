class ZoomController:
    def __init__(self, min_dist=30, max_dist=250, min_scale=1.0, max_scale=3.0):
        self.min_dist = min_dist
        self.max_dist = max_dist
        self.min_scale = min_scale
        self.max_scale = max_scale

    def get_zoom_scale(self, distance):
        distance = max(self.min_dist, min(distance, self.max_dist))
        scale = self.min_scale + (distance - self.min_dist) * (self.max_scale - self.min_scale) / (self.max_dist - self.min_dist)
        return round(scale, 2)
