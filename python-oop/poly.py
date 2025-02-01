class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method")


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Function demonstrating polymorphism


def animal_sound(animal):
    print(animal.make_sound())


# Create instances
dog = Dog()
cat = Cat()
cow = Cow()

# Different objects, same method call
animal_sound(dog)  
animal_sound(cow)
animal_sound(cat)


class Vehicle:
    def start(self):
        raise NotImplementedError("Subclass must implement this method")


class Car(Vehicle):
    def start(self):
        return "Car engine starts with a roar!"


class Bike(Vehicle):
    def start(self):
        return "Bike engine starts with a rev!"


class ElectricCar(Vehicle):
    def start(self):
        return "Electric car starts silently!"

# Function demonstrating polymorphism


def start_vehicle(vehicle):
    try:
        # Check if the object is an instance of Vehicle or its subclass
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Invalid vehicle type")
        print(vehicle.start())
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Create instances
car = Car()
bike = Bike()
electric_car = ElectricCar()
vehicle = Vehicle()


# Same method, different implementations based on the object type
start_vehicle(car)           # Outputs: Car engine starts with a roar!
start_vehicle(bike)          # Outputs: Bike engine starts with a rev!
start_vehicle(electric_car)  # Outputs: Electric car starts silently!
start_vehicle(vehicle)
