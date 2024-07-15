class Car:
    # Constructor
    def __init__(self, brand, model,colour):
        #  if we have to make an attribute private we can:
        #  self.__brand = brand # by adding __brand it makes the variable private
         self.__brand = brand
         self.model=model
         self.colour=colour
    
    # getter method to access private data of a class
    def get_brand(self):
        return self.__brand


    # create methods and access those methods in cild class
    def print_full_name(self):
         return f"{self.brand} {self.model} {self.colour}"
#Inheritance 
class ElectricCar(Car):
     def __init__(self, brand, model, colour, battery_size):
          super().__init__(brand, model, colour) 
          self.battery_size= battery_size
         

# Objects
# audi_car = Car("Audi", "R8", "White")         
# lambo_car = Car("Lamborghini", "Evo Spider", "Black")         
# bmw_car = Car("BMW", "M4", "Blue")  

# print("full name of car is: ")
# print(audi_car.print_full_name())

# print("Audi: ")
# print(audi_car.brand, " ", audi_car.model, " ", audi_car.colour)

# print("=======================================================")

# print("BMW: ")
# print(bmw_car.brand, " ", bmw_car.model, " ", bmw_car.colour)

# print("=======================================================")

# print("Lamborghini: ")
# print(bmw_car.brand, " ", bmw_car.model, " ", bmw_car.colour)

# print("  ")
# print("-----------END----------")

# Electric car object

tesla_electric = ElectricCar("Tesla", "Model S", "White", "120KWh")

# print("Electric tesla")
# print(tesla_electric.brand, " ", tesla_electric.model, " ", tesla_electric.colour, " ", tesla_electric.battery_size)

# Calling the parent class methods from child object reference
# print(tesla_electric.print_full_name())

print(tesla_electric.get_brand())