class Animal_RBH:
    def speak_RBH(self_RBH):
        print("Animal makes a sound")

class Dog_RBH(Animal_RBH):
    def speak_RBH(self_RBH):
        print("Dog barks")

class Cat_RBH(Animal_RBH):
    def speak_RBH(self_RBH):
        print("Cat meows")

animals_RBH = [Dog_RBH(), Cat_RBH()]
for animal_RBH in animals_RBH:
    animal_RBH.speak_RBH()
