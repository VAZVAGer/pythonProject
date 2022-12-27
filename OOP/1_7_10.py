class AppStore:
    def __init__(self):
        self.Application_list = []

    def add_application(self, app):
        self.Application_list.append(app)

    def remove_application(self, app):
        self.Application_list.remove(app)

    def block_application(self, app):
        for i in self.Application_list:
            if i == app:
                i.fl_like = True

    def total_apps(self):
        return len(self.Application_list)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked
