class Car:
    def __init__(self, brand, model, year):
        self.brand_EIV = brand
        self.model_EIV = model
        self.year_EIV = year

    def display_car(self):
        print(self.brand_EIV, self.model_EIV, self.year_EIV)


car1 = Car("Toyota", "Corolla", 2020)
car1.display_car()

