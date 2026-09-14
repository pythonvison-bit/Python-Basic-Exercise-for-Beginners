'LOOPS IN Python'

# While

i = 1

while (i < 51): 

    print(i)

    i += 1

l = ["apple", "mango", "banana", "gauva", "watermelon"]

item = 0

while (item < len(l)):
    print(l[item])
    item += 1


'for loop in python'
 
l = [1,11,222,555,121,43]

for num in l:
    print(num)


"using else in for loops"

l = [1,55,44,6]
for num in l:
    print(num)
else:
    print ("Done Bro")

"using Break in For loops"

N = (1,22,33,55,29)

for num in N:
    print(num)
    if num == 33:
        break

"Continue in for loops"

n = (1,33,55,65)
for num in n:
    print(num)
    if num == 33:
        continue

"pass method in for loops"

a = ("ssa","dssd","dsdsd")
for item in a:
    pass

i = 1
for i in range(1, 50):
    print(i)

"making a calculator table"

a = int(input("Enter your table: "))

for num in range(1, 11):
    print(f"{a} x {num} = {a * num}")

# second code

l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"{name}")

# write a tabe but twist is in while loop.

a = int(input("enter the table"))
b = 1
while (b<11):
    print(f"{a * b}")

    b += 1

"making a star partern"
