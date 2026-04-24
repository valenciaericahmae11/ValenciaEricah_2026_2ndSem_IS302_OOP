class Person_EIV:
    def __init__(self_EIV, name_EIV, age_EIV):
        self_EIV.__name_EIV = name_EIV
        self_EIV.__age_EIV = age_EIV

    def get_name_EIV(self_EIV):
        return self_EIV.__name_EIV

    def get_age_EIV(self_EIV):
        return self_EIV.__age_EIV

p1_EIV = Person_EIV("Maria", 20)
print("Name:", p1_EIV.get_name_EIV())
print("Age:", p1_EIV.get_age_EIV())
