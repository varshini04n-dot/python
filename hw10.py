from abc import ABC, abstractmethod

class user(ABC):
    def __init__(self,name,joining_year):
        self.name = name
        self.joining_year = joining_year
    def calculate_years(self):
        return 2025 - self.joining_year
    @abstractmethod
    def get_role(self):
        pass
class customer(user):
    def __init__(self,name,joining_year):
        super().__init__(name, joining_year)
        self.role = "VIP"
    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}, Years: {self.calculate_years()}"
    def get_role(self):
        return self.role
    
class vendor(user):
    def __init__(self,name,joining_year):
        super().__init__(name, joining_year)
        self.role = "Seller"
    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}, Years: {self.calculate_years()}"
    def get_role(self):
        return self.role
obj1=customer("Varshii", 2020)
obj2=vendor("Alice", 2021)
print(obj1)
print(obj2)
print(obj1.get_role())
print(obj2.get_role())
