class Server:
    counter_server = 0

    def __init__(self):
        self.buffer = []
        self.ip = self.counter_server + 1
        self.counter_server = self.ip


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
