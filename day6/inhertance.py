class BaseClass():
    def __init__(self):
        print("base ile init")

    def set_name(self, name):
        self.name = name
        print("base set")

    def display_name(self):
        print("name is " + self.name)


class SubClass(BaseClass):
    def __init__(self):
        super().__init__()
        print("sub ile init")

    def set_name(self, name):
        self.name = name
        print("subile set")

    def welcome(self):
        print("welcomes you")


x = SubClass()
x.set_name("shuaib")
x.display_name()
x.welcome()
