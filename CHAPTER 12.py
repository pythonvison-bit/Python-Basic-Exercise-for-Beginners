# ADVANCE PYTHON 1

# Walrus method

if (age := 18) > 17:
    print(f"age is {age} and you are allowed to enter")

# type defination in python

"age: str = 18 "
"str." # it allow to show all the methods of str class

"age: int = 18"
"int." # it allow to show all the methods of int class


# Match case statement in python

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 500:
            return "Internal Server Error"
        case 403:
            return "not allowed"
        case _:
            return "Something's wrong with the internet"


print(http_status(403)) 


# List comprehension in python

list1 = [1, 2, 3, 4, 5]
squaredlist = [i**2 for i in list1]

print(squaredlist)

# PRINT TABLE OF 5 USING LIST COMPREHENSION

A = int(input("Enter the number to print table: "))
N = A
TABLE = [N * i for i in range(1, 11)]
print(TABLE)