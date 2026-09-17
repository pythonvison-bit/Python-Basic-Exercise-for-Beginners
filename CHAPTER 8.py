
"using def function in python"

# Function Definition

def d():
    a = int(input("enter the first num:"))
    b = int(input("enter the first num:"))
    c = input("enter your operation: +,-,* ")

    if  '+':
        print(a+b)
    elif '-':
        print(a-b)
    else:
       print("error")

# function call

d()
d()
d()

# ouick quiz 

def niceday (name, ending):
    print("nice Day, "+ name)
    print(ending)

niceday("abhijeet", "Thankyou")
niceday("ashmita", "Thankyou")
niceday("ranveer", "Thankyou")

# return method

def niceday (name, ending):
    print("nice Day, "+ name)
    print(ending)

    return("ok")

a = niceday("abhijeet", "Thankyou")
print(a)


