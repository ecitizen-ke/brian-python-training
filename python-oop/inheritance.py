# inheritance involves - creating new classes based on existingmclases 

#  a car is a vehicle
#  a bike is a vehicle

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def start(self):
        print("vehicle is starting")    
    def stop(self):
        print("vehicle is stopping")    
class Car(Vehicle):
    def __init__(self, brand, model, year, wheels, color):
        super().__init__(brand, model, year),
        self.wheels= wheels
        self.color= color
class Bike(Vehicle):
    def __init__( self, brand, model, year, wheels):
        super().__init__(brand, model, year)
        self.wheels = wheels
vehicle1 = Vehicle("toyota", "xxx", 2013)        
bike1 = Bike("mountain_bike", "small", 2012, 2)
car1 = Car("Ford", "Focus", 2008, 4, "red") 

print(vehicle1.__dict__)
print(car1.__dict__)
print(car1.year)  
print(vehicle1.year)   
print(bike1.__dict__)
car1.start()
vehicle1.stop()
bike1.start

