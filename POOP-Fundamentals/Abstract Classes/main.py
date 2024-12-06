from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")


car = Car()
car.go()
car.stop()


class Motorcycle(Vehicle):
    def go(self):
        print("You drive the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()



class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You stop the boat")

boat = Boat()
boat.go()
boat.stop()