class First():
    def display_first(self):
        print("hi")


class Second(First):
    def display_second(self):
        print("hello")


class Third(Second):
    def display_third(self):
        print("third")


x = Third()
x.display_first()
x.display_second()
x.display_third()

print(Third.mro())
