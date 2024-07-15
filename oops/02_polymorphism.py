class Car:
    def __init__(self, brand, model) :
        self.brand=brand
        self.model=model

    def print_full_name(self):
        return f"{self.brand} {self.model}"   

    def fuel_type(self):
        return "Diesel Or Petrol"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size= battery_size

    def fuel_type(self):
      return  super().fuel_type()
        # return "Electric Charge"    


# audi_car = Car("Audi", "R8")     
# print(audi_car.fuel_type())

tesla_car = ElectricCar("Tesla", "Model S", "120KWh")
print(tesla_car.fuel_type())