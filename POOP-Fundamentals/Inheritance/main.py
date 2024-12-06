class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")



class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def spek(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")


dog = Dog("Cookie")
cat = Cat("Venga")
mouse = Mouse("Capitalism")

print(cat.name)
print(cat.is_alive)
dog.sleep()
dog.eat()

dog.speak()