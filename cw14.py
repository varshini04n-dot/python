import random
import math
guests=int(input("Enter the number of students: "))
guest=[]
for x in range(0,guests):
    name=input("enter the students name: ")
    guest.append(name)

og_guest=[]
for x in guest:
    if x not in og_guest:
        og_guest.append(x)
print("removing duplicates: ",og_guest)
random_guest=random.choice(og_guest)
str=""
for i in random_guest:
    str=i+str
print("reverse str:", str)
unique=len(og_guest)
print("unique name:",unique)
square=math.sqrt(unique)
print("square root: ",round(square))


    
