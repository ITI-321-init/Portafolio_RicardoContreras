from pyatspi import STATE_IS_DEFAULT


class Student:

    count = 0
    total_id = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id
        Student.count += 1
        Student.total_id += id

    #INSTANCE METHOD
    def get_info(self):
        return f'{self.name}, {self.id}'


    @classmethod
    def get_count(cls):
        return f'total number of Students: {cls.count}'

    @classmethod
    def get_average(cls):
        if cls.count == 0:
            return 0
        else:
            return f'Average: {cls.total_id / cls.count:.2f}'


student1 = Student('Gojo', 1.1)
student2 = Student('NADIE', 2.2)
student3 = Student('Itadori', 3.3)
student4 = Student('TAMBIEN NADIE', 4.4)

print(Student.get_count())

print(Student.get_average())



