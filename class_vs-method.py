class Employee:
    company_name="ostad company"
    def __init__(self,name,salary):
        self.name=name 
        self.salary=salary
    
    def display_info(self):
        print( f"EMp name ${self.name} \n Salary ${self.salary}")    
    @classmethod
    def change_company_name(cls,name):
        cls.company_name=name
        
ob1=Employee("Rahim",30000)
ob1.display_info()
ob1.change_company_name("ABC company")
print(ob1.company_name)          