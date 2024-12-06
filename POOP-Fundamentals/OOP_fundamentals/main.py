from car import Car

car1 = Car('Mercedes-Benz', 2009, 'blue', True)
car2 = Car('Toyota Raize', 2023, 'red', False)
car3 = Car('Toyota Hilux', 2024, 'White', True)

print(car1.model)
print(car2.year)
print(car3.color)
print(car1.for_sale)

car1.drive()
car2.stop()

car1.describe()
