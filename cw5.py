python={"Varsh","kows","bismi"}
datascience={"sanji","kows","nithi"}
python.add("prathi")
datascience.remove("nithi")
print(python&datascience)
print(python-datascience)
print(python|datascience)
course={"Python":len(python),"Data Science":len(datascience)}
for x ,y in course.items():
    print("Course",":",x,",""Students",":",y)
newdic={x:y*2 for x,y in course.items()}
print(newdic)
