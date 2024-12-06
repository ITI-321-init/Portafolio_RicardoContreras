class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position


    def get_info(self):
        return f'{self.name}, {self.position}'



    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Coocker', 'Casheir', 'Janitor']
        return position in valid_positions

employee1 = Employee('Mr Krabs', 'Manager')
employee2 = Employee('Sponge Bob', 'Coocker')
employee3 = Employee('Squidward', 'Casheir')




print(Employee.is_valid_position('Coocker'))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())