class FileAcceptor:
    def __init__(self, *args):
        self.extension = [args]

    def __call__(self, argument):
        extension_arg = argument[argument.rfind('.') + 1::]
        if extension_arg in self.extension:
            return True
        else:
            return False

    def __add__(self, other):
        if isinstance(other, FileAcceptor):
            return FileAcceptor(*(self.extension + other.extension))


filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
ff = [filter(acceptor_images + acceptor_docs, filenames)]
print(ff)

