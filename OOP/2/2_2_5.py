class WindowDlg:
    def __init__(self, title, width, heidht):
        self.__title = title
        self.__width = width
        self.__height = heidht

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, vel):
        if type(vel) == int and 0 <= vel <= 10000:
            if self.__width:
                self.show()
            self.__width = vel

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, vel):
        if type(vel) == int and 0 <= vel <= 10000:
            if self.__height:
                self.show()
            self.__height = vel
