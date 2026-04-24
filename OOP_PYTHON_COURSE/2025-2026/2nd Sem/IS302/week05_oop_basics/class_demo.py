class Person:
    def __init__(self, name, age):
        self.name_EIV = name
        self.age_EIV = age

    def display_info(self):
        print("Name:", self.name_EIV)
        print("Age:", self.age_EIV)


p1 = Person("Juan", 20)
p1.display_info()

