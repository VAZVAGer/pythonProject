class Track:
    def __init__(self, start_x, start_y):
        self.track = [TrackLine(start_x, start_y, 0)]

    def add_track(self, tr):
        self.track.append(tr)

    def get_tracks(self):
        return tuple(self.track)

    def __len__(self):
        if len(self.track) < 2:
            return 0
        l_e_n = 0
        for i in range(len(self.track) - 1):
            section_of_track = (self.track[i:i + 2])
            l_e_n += ((section_of_track[-1].x - section_of_track[0].x) ** 2 +
                      (section_of_track[-1].y - section_of_track[0].y) ** 2) ** 0.5
        return int(l_e_n)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)
    def __gt__(self, other):
        return len(self) > len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.x = to_x
        self.y = to_y
        self.speed = max_speed


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = (track1 == track2)
