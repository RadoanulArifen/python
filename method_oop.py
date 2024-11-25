class Student:
    roll=""
    gpa=""
    def __init__(self,name,address,id):

        self.amr_name=name
        self.amr_bari=address
        self.amr_id=id
    

Arifen=Student("Arifen Fahim","Cumilla",1234)
print(Arifen.amr_name, Arifen.amr_bari,Arifen.amr_id)



class Car:
    pass
    def set_value(self,color,speed):
        self.car_color=color
        self.car_speed=speed
    
    def display(self):
        print(f"Color:{self.car_color},\tSpeed:{self.car_speed}")

bugatti=Car()
bugatti.set_value("red",200)
bugatti.display()

lambor=Car()
lambor.set_value("Green",500)
lambor.display()



class circle:
    base=""
    height=""

    def __init__(self,base,height):
        self.circle_base=base
        self.circle_height=height
    
    def area(self):
        area=0.5*self.circle_base*self.circle_height
        print(area)

Circle=circle(10,20)
Circle.area()


        