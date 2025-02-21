class Employee:
    company_name="ostad company"
    def __init__(self,name,salary):
        self.name=name 
        self._salary=salary  #by convention,_veriable mmeans private but logically this is not a private or protected veriable

    def get_salary(self,password):
        if password=="Admin":
            print(self._salary)
        else:
            print("Invalid password")
    
    def set_salary(self,password,salary):
        if password=="Admin":
            self._salary=salary
            print(f"new salary: {self._salary}")
        else:
            print("Invalid password")       
            
ob1=Employee("Rahim",30000)
ob2=Employee("Korim",2000)

ob1.get_salary("Admin")
print(ob1._salary)

ob1.set_salary("Admin",60000)