class Car:
    def __init__(self):
        self.brad=""
        self.model=""
    
car1 = Car()
car1.brad="BMW"
car1.model="7CD"
print(f"car brand is ${car1.brad} \ncar model is ${car1.model}")



class Carr:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def __str__(self):
        return f"Car Brand: {self.brand}, Model: {self.model}"
    
car2 = Carr("Hybride","5BC")
print(car2)