# ADVANCE PYTHON PROGRAMMING 2

# LAMBDA FUNCTION

square = lambda X: X * X
print(square(7))

# Join Method
a = ["abhijeet", "ranjan", "kumar", "singh"]
final = "-".join(a)
print(final)

# String methods
name = "abhijeet kumar"
print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("kumar", "singh"))
print(name.split())

# List methods
numbers = [3, 1, 4, 2]
numbers.append(5)
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.pop()
print(numbers)

# Dictionary methods
student = {"name": "Abhijeet", "course": "Python", "year": 2026}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
