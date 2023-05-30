class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return (self.hours * 3600) + (self.minutes * 60) + self.seconds


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        sec = self.__len__()
        sec = sec % (24 * 3600)
        hour = sec // 3600
        sec %= 3600
        min1 = sec // 60
        sec %= 60
        return f'{hour:02}: {min1:02}: {sec:02}'


    def __len__(self):
        sec = self.clock1.get_time() - self.clock2.get_time()
        if sec < 0:
            return 0
        return sec
