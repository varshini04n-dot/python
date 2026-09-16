class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_details(self):
        print("Person Name:",self.name)
        print("Person Age:",self.age)
class employee(person):
    def __init__(self, name, age, employee_id):
        person.__init__(self,name, age)
        self.employee_id=employee_id
    def show_details(self):
        print("employee name:",self.name)
        print("employee age:",self.age)
        print("employee id:",self.employee_id)
class PartTime(person):
    def __init__(self, name, age, working_hours):
        person.__init__(self,name, age)
        self.working_hours=working_hours
    def show_details(self):
        print("Worker's Name:",self.name) 
        print("Age:",self.age)
        print("Working Hours:",self.working_hours)
class consultant(employee,PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        person.__init__(self,name, age)
        self.employee_id=employee_id
        self.working_hours=working_hours
        self.project_name=project_name
    def show_details(self):
        print("Consultant Name:",self.name)
        print("Age:",self.age)
        print("Employee ID:",self.employee_id)
        print("Working Hours:",self.working_hours)
        print("Project Name:",self.project_name)
obj1=person("John",30)
obj2=employee("Alice", 25, 101)
obj3=PartTime("Bob", 35, 20)
obj4=consultant("Charlie", 40, 102, 25, "Project X")

obj1.show_details()
obj2.show_details()
obj3.show_details()
obj4.show_details()

    