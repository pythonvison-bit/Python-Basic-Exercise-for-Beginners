# CHAPTER 11: OBJECT-ORIENTED PROGRAMMING (OOP)


# 1. SINGLE INHERITANCE
# Programmer inherits the attributes and methods of Employee.
class Employee:
    company = "Bright Tech"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")


class Programmer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)  # Call the Employee constructor.
        self.language = language

    def write_code(self):
        print(f"{self.name} writes code in {self.language}.")


programmer = Programmer("Asha", 75000, "Python")
programmer.show_details()  # Inherited from Employee.
programmer.write_code()


# 2. MULTIPLE INHERITANCE
# Child inherits methods from both ParentOne and ParentTwo.
class ParentOne:
    def teach_math(self):
        print("Parent one teaches mathematics.")


class ParentTwo:
    def teach_art(self):
        print("Parent two teaches art.")


class Child(ParentOne, ParentTwo):
    pass


child = Child()
child.teach_math()
child.teach_art()


# 3. MULTILEVEL INHERITANCE
# Manager inherits from Employee, and Employee inherits from Person.
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")


class StaffMember(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def show_id(self):
        print(f"Employee ID: {self.employee_id}")


class Manager(StaffMember):
    def approve_leave(self):
        print(f"{self.name} can approve leave requests.")


manager = Manager("Ravi", "E104")
manager.introduce()
manager.show_id()
manager.approve_leave()


# 4. METHOD OVERRIDING AND POLYMORPHISM
# A child class can provide its own version of a parent method.
class Animal:
    def speak(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def speak(self):
        print("The dog barks.")


class Cat(Animal):
    def speak(self):
        print("The cat meows.")


animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()  # The method that runs depends on the object's class.


# 5. CLASS METHOD
# A class method works with the class rather than one particular object.
class Student:
    school = "Sunrise School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


Student.change_school("Riverdale School")
student = Student("Meena")
print(f"{student.name} studies at {student.school}.")


# 6. PROPERTY: GETTER AND SETTER
# The property lets us use student_name like an attribute while
# keeping validation in the setter.
class StudentRecord:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = value.strip()


record = StudentRecord("  Isha  ")
print(record.name)  # Calls the getter.
record.name = "Neel"  # Calls the setter.
print(record.name)


# 7. OPERATOR OVERLOADING
# Dunder (double-underscore) methods define how operators work for objects.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        return Vector(self.x * number, self.y * number)

    def __truediv__(self, number):
        return Vector(self.x / number, self.y / number)

    def __floordiv__(self, number):
        return Vector(self.x // number, self.y // number)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __len__(self):
        return 2  # A two-dimensional vector has two coordinates.


first = Vector(8, 6)
second = Vector(2, 3)
print("Addition:", first + second)  # Calls first.__add__(second).
print("Subtraction:", first - second)
print("Multiply by 2:", first * 2)
print("Divide by 2:", first / 2)
print("Floor divide by 2:", first // 2)
print("Number of coordinates:", len(first))  # Calls first.__len__().
print("String form:", str(first))  # Calls first.__str__().
