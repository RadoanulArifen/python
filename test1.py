class shape:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    
    def area(self):
        print("I am area method of shape class")


class triangle(shape):
    def area(self):
        super().area()
        area=0.5*self.dim1*self.dim2
        print("Area of triangrl",area)


class rectriangle(shape):
    def area(self):
        area=self.dim1*self.dim2
        print("Area of Rectriangrl",area)

T1=triangle(10,20)
R1=rectriangle(10,20)

T1.area()
R1.area()