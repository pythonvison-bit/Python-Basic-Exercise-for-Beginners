D = {"rohan":100
     ,"sohan":200
     ,"mohan":100
     }

print(D["mohan"])

# .update method

D = {"rohan":100
     ,"sohan":200
     ,"mohan":300}

D.update({"rohan":400})
print(D["rohan"])

# .get method

D = {"rohan":100
     ,"sohan":200
     ,"mohan":300}

print(D.get("hdsgd"))

# .items method


D = {"rohan":100
     ,"sohan":200
     ,"mohan":300}

print(D.items())
print(D)

# .keys method
# .update method

D = {"rohan":100
     ,"sohan":200
     ,"mohan":300}

print(D.keys())


'''SET METHODS'''

# Empty set

s = set()
print(type(s)) 

s = {1,2,3,2,4,45}
print(s)

# methods of sets

s = {"abhijeet",22}
s.add("rohan")
print(s)



# Disctonary book

Books = {"sab": "apple",
         "angur": "grapes",
         "anda": "mango",
         "pyaaz": "onion"}

book= input("Enter the word you want to translate: ")
print(Books.get(book, "We don't have this word"))
