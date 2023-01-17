class Router:

    def __init__(self):
        self.buffer = []
        self.list_of_connected_servers = {}

    def link(self, server):  # Для присоеденения сервера к роутеру.
        self.list_of_connected_servers[server.ip] = server

    def unlink(self, server):  # Для отсоединения сервера server (объекта класса Server) от роутера
        s = self.list_of_connected_servers.pop(server.ip, False)

    def send_data(
            self):  # Для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам (после отправки буфер должен очищаться).
        for mes in self.buffer:
            if mes.ip in self.list_of_connected_servers:
                self.list_of_connected_servers[mes.ip].buffer.append(mes)
        self.buffer.clear()


class Server:  ## Вроде готов!
    counter_server = 0

    def __init__(self):
        self.buffer = []
        self.ip = Server.counter_server + 1
        Server.counter_server = Server.counter_server + 1

    def send_data(self, data):
        router.buffer.append(data)

    def get_data(self):
        buf_c = self.buffer[:]
        self.buffer.clear()
        return buf_c

    def get_ip(self):
        return self.ip


class Data:  ## Класс готов.
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router,
                                                                         'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server,
                                                                                'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"
print(len(msg_lst_to))
assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

assert msg_lst_from[0].data == "Hi" and msg_lst_to[
    0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"

assert hasattr(router, 'buffer') and hasattr(sv_to,
                                             'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"

router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()
assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"
