# .read command.
file = open("file.txt")
data = file.read()
print(data)
file.close()

# .write command.
string = "hello wow i am learning ch = 9"
f = open("myfile.txt", "w")
f.write(string)
f.close()

# with statement
with open("myfile.txt", "r") as f:
    data = f.read()
print(data)

