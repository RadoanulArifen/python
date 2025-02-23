#assocation
class Laptop:
    def __init__(self,brand):
        self.brand=brand
    
class Student:
    def __init__(self,name,laptop_obj):
        self.name=name
        self.laptop_v=laptop_obj
    
    def show_laptop_info(self):
        print(f"{self.name} has a laptop named {self.laptop_v.brand}")

lp1=Laptop("Asus")
std=Student("Arifen",lp1)
std.show_laptop_info()

#Aggrigation
class Department:
    def __init__(self,name):
        self.name=name

class University:
    def __init__(self,name):
        self.name=name
        self.departments=[]
    def add_department(self,department):
        self.departments.append(department)
    
    def show_department(self):
        return [department.name for department in self.departments]
    
uni1=University("DIU")
dep1=Department("CSE")
dep2=Department("SWE")
uni1.add_department(dep1)
uni1.add_department(dep2)
print(uni1.show_department( ))