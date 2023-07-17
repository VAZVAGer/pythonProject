class Track:
    def __init__(self, start_x, start_y):
        self.track = ((start_x, start_y, 0),)

    def add_track(self, tr):
        self.track += tr.self.self.trackline

    def get_tracks(self):
        return self.track



class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.trackline = ((to_x, to_y, max_speed),)
