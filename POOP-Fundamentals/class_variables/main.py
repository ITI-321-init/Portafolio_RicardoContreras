

class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Ricardo", 22)
student2 = Student("Daniel", 23)
student3 = Student("Angel", 24)
student4 = Student("Ferreto", 25)

print(student2.name)
print(student2.age)
print(Student.class_year)
print(Student.num_students)

print(f"My graduating class of {Student.class_year} is {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)