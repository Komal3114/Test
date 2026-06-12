f = open("test.txt","w")
f.write("Hello World")
f.close()
print("File Created!")

f = open("test.txt","r")
constant = f.read()
print(constant)
f.close()

f = open("test.txt","a")
f.write("\n new line added")
f.close()
print("Data Added")

"""
with open("student.txt","w") as f:
    f.write("Rahul - 85\n")
    f.write("Prakit - 35\n")
    f.write("Kritika - 24\n")
    f.write("Krish - 95\n")
    f.write("Raj - 45\n")
print("data is written")
"""