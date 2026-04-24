class Animal_EIV:
    def __init__(self_EIV, name_EIV):
        self_EIV.name_EIV = name_EIV

    def speak(self_EIV):
        print(self_EIV.name_EIV, "makes a sound")

class Dog_EIV(Animal_EIV):
    def bark(self_EIV):
        print(self_EIV.name_EIV, "barks")

dog1_EIV = Dog_EIV("Buddy")
dog1_EIV.speak()
dog1_EIV.bark()
