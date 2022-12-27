class Viber:
    def __init__(self):
        self.list_msg = []
    def add_message(self, msg):
        self.list_msg.append(msg)

    def remove_message(self, msg):
        self.list_msg.remove(msg)
    def set_like(self, msg):
        for i in self.list_msg:
            if i == msg:
                if i.blocked == False:
                    i.blocked = True
                elif i.blocked == True:
                    i.blocked == False

    def show_last_message(self, number):
        for mes in self.list_msg[-number:]:
            print(mes)
    def total_messages(self):
        return len(self.list_msg)

class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like
