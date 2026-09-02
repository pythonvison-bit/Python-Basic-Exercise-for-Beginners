'list'

list = ["milk", "juice", "cake"]
 
print(list[0])

list[0]= "apple"     

print (list)

# list methods = .append 
a = ["mango", "grapes","papaya"]
a.append("apple")
print(a)

# .sort
list = ["11", "2", "3"]
list.sort()
print(list)

#.reverse
list = ["99", "44", "55"]
list.reverse()
print(list)


# .remove
list = ["coconut", "banana", "apple"]
list.remove("banana")
print(list)

#.insert
l = ["sweets","snacks","icecream"]
l.insert(1, "chocolates")
print(l)

'''tuple in python'''

a = (1, 23, 4, 5)
print(type(a))

# methods in tuple

a = (1, 2, 3, 4, 5)
print(a.count(2)) # its count of number.

a = (1, 2, 3, 4, 5)
print(a.index(3)) # it show of position


# pratice of chapter 4

fruits_list = [input("Enter of fruits name: "),
                input("Enter of second fruit name: "),
                input("Enter of third fruit name: "),
                input("Enter of fourth fruit name: "),
                input("Enter of fifth fruit name: "),
                input("Enter of sixth fruit name: ")]
print(fruits_list)


marks = [int(input("Enter of marks for student 1: ")),
                int(input("Enter of marks for student 2: ")),
                int(input("Enter of marks for student 3: ")),
                int(input("Enter of marks for student 4: ")),
                int(input("Enter of marks for student 5: ")),
                int(input("Enter of marks for student 6: "))]

marks.sort()
print(marks)


l = [1, 2, 3, 4, 5]
l = sum(l)
print(l)