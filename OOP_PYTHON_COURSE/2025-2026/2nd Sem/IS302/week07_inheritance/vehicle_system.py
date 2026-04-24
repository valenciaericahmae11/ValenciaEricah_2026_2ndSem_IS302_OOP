class Vehicle_EIV:
    def __init__(self_EIV, brand_EIV, model_EIV):
        self_EIV.brand_EIV = brand_EIV
        self_EIV.model_EIV = model_EIV

class Car_EIV(Vehicle_EIV):
    def __init__(self_EIV, brand_EIV, model_EIV, year_EIV):
        super().__init__(brand_EIV, model_EIV)
        self_EIV.year_EIV = year_EIV

    def display_car_EIV(self_EIV):
        print(self_EIV.brand_EIV, self_EIV.model_EIV, self_EIV.year_EIV)

car1_EIV = Car_EIV("Toyota", "Corolla", 2022)
car1_EIV.display_car_EIV()
