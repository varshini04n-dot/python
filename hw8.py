class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Employee Name:", self.name)
        print("Role:", self.role)


class Trainer(Employee):
    def __init__(self, name, specialization):
        Employee.__init__(self, name, "Trainer")
        self.specialization = specialization

    def display(self):
        print("Trainer Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)


class YogaInstructor(Employee):
    def __init__(self, name, yoga_style):
        Employee.__init__(self, name, "Yoga Instructor")
        self.yoga_style = yoga_style

    def display(self):
        print("Yoga Instructor Name:", self.name)
        print("Role:", self.role)
        print("Yoga Style:", self.yoga_style)


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, specialization, yoga_style):
        Employee.__init__(self, name, "Multi Trainer")
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print("Multi Trainer Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)


obj1 = Employee("Alice", "Manager")
obj2 = Trainer("John Doe", "Fitness")
obj3 = YogaInstructor("Jane Smith", "Hatha")
obj4 = MultiTrainer("David", "Nutrition", "Vinyasa")

obj1.display()
obj2.display()
obj3.display()
obj4.display()