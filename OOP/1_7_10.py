class AppStore:
    Application_list = []

    def add_application(self, app):
        self.Application_list.append(app)

    def remove_application(self, app):
        self.Application_list.remove(app)

    def block_application(self, app):
        pass

    def total_apps(self):
        return len(self.Application_list)
