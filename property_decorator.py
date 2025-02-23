class Employee:
    company_name="ostad company"
    def __init__(self,name,salary):
        self.name=name 
        self._salary=salary
    
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,new_salary):
        self._salary = new_salary
ob1=Employee("Rahim",40000)
print(ob1.salary)

ob1.salary=70000
print(ob1._salary)