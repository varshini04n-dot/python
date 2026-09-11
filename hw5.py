frontend={"varshini","kows","bismi","raji"}
backend={"sanji","kows","isaa"}
backend.add("mathew")
frontend.remove("raji")
print(frontend&backend)
print(backend-frontend)
print(len(frontend^backend))
course={"Frontend":len(frontend),"Backend":len(backend)}
for x,y in course.items():
    print(x,y)
newdic={x:y for x,y in course.items()}
newdic["Full Stack"]=len(frontend)+len(backend)
print(newdic)