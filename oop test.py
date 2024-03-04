class circul:
    base=""
    hight=""

    def __init__(self,base,hight):

        self.base=base
        self.hight=hight
    
    def area_of_circle(self):
        area=0.5*self.base*self.hight
        print(f"Area: {area}")

t1=circul(10,20)
t1.area_of_circle()

t2=circul(30,40)
t2.area_of_circle()