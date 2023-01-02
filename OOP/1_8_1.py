class Router:
    def __init__(self):
        buffer = []
        list_of_connected_servers = []

    def link(self, server):  # Для присоеденения сервера к роутеру.
        self.list_of_connected_servers.append(server)

    def unlink(self, server):  # Для отсоединения сервера server (объекта класса Server) от роутера
        self.list_of_connected_servers.remove(server)

    def send_data(self):  # Для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам (после отправки буфер должен очищаться).
        for data in self.buffer:
            msg = data.self.data
            address = data.self.ip


class Server:
    counter_server = 0

    def __init__(self):
        self.buffer = []
        self.ip = Server.counter_server + 1
        Server.counter_server = Server.counter_server + 1


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

sv_from = Server()
sv_from2 = Server()
sv_from3 = Server()
print(sv_from.ip)
print(sv_from2.ip)
print(sv_from3.ip)
