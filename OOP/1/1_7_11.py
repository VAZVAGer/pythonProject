class Viber:
    list_msg = []
    @classmethod
    def add_message(cls, msg):
        cls.list_msg.append(msg)
    @classmethod
    def remove_message(cls, msg):
        cls.list_msg.remove(msg)
    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like
    @classmethod
    def show_last_message(cls, number):
        for mes in cls.list_msg[-number:]:
            print(mes)
    @classmethod
    def total_messages(cls):
        return len(cls.list_msg)

class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like
