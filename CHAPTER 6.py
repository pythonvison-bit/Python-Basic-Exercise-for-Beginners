# if elif else ladder 
a = int(input("enter your age: "))

if(a>18):
    print("good you are above of 18")

elif(a<0):
    print("bro where is your mind: ")

else:
    print("sorry you are not above of 18")


a = int(input("enter the first num: "))
b = int(input("enter the  second num: "))
c = input("enter your operation")
if c == '+': 
    print(a+b)
elif c == '-':
    print(a-b)

elif c== '*':
    print(a*b)
elif c== '/':
    print(a/b)

else: 
    print("please write vailed input 😊.")