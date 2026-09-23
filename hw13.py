students=int(input("Enter the number of students: "))
for x in range (0,students):
    name=input("enter the students name:  ")
    f=open("student.txt","a")
    f.write(name+"\n")
    f.close()
a=open("student.txt","r")
print(a.read())
b=open("student.txt","a")
b.write("bismi")
c=open("student.txt","r")
print(c.read())


