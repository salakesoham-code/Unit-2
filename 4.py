# Base Class
class Vehicle:
    def move(self):
        print("Vehicle is moving")


# Subclass 1
class Car(Vehicle):
    def move(self):
        print("Driving on the road")


# Subclass 2
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")


# Demonstrating Polymorphism
def show_movement(vehicle):
    vehicle.move()


# Creating objects
car1 = Car()
bicycle1 = Bicycle()

# Calling move() using polymorphism
show_movement(car1)
show_movement(bicycle1)
