class Grandfather:
    def greet(slef):
        print("Grandfather says")

class Father(Grandfather):
    def greet(self):
        print("Father syas")

class child(Father):
    def greet(self):
        print("Chid says")

gf = Grandfather()
f=Father()
c=child()

gf.greet()
f.greet()
c.greet()

#method overloading
class Shape:
    def area(self,a,b=10):
        return a*b
  

s=Shape()
print(s.area(10))
print(s.area(10,12))