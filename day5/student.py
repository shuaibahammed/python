class Student:
    year = 2020

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def add_age(self):
        self.age = self.age + 1

    def relocate(self):
        self.place = place

    def display(self):
        print("year :" + str(Student.year))
        print("name :" + self.name)
        print("age :" + str(self.age))
        print("place :" + self.place)

    @classmethod
    def add_year(cls):
        cls.year=cls.year+1

    @staticmethod
    def welcome():
        print("welcome you")

Student.welcome()

x = Student("shuaib", 21, "mlp")
y = Student("shahd", 40, "kannr")


x.display()
y.display()
print("============================")
Student.year = Student.year + 1

x.add_age()
y.add_age()



x.display()
y.display()

print("-------------")
Student.welcome()
Student.add_year()



x.add_age()
y.add_age()



x.display()
y.display()



