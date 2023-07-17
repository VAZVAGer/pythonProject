class Track:
    def __init__(self, start_x, start_y):
        self.track = ((start_x, start_y, 0),)

    def add_track(self, tr):
        self.track += tr.self.self.trackline

    def get_tracks(self):
        return self.track

    def __len__(self):
        if len(self.track) < 2:
            return 0
        l_e_n = 0
        for i in range(len(self.track) - 1):
            print(self.track[i:i + 2])
            time_t = (self.track[i:i + 2])
            l_e_n += ((time_t[-1][0] - time_t[0][0]) ** 2 + (time_t[-1][-1] - time_t[0][-1]) ** 2)
        return l_e_n


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.trackline = ((to_x, to_y, max_speed),)

# track1 = Track(0, 0)
# track1.add_track(TrackLine(2, 4, 100))
# track1.add_track(TrackLine(5, -4, 100))
#
# track2 = Track(0, 1)
# track2.add_track(TrackLine(3, 2, 90))
# track2.add_track(TrackLine(10, 8, 90))
