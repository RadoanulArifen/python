#parent class/super class
class phone:
    def color(self):
        print("Color is green")
    def call(self):
        print("You can call")

#child clas/sub class
class samsumg(phone):
    def photo(self):
        print("Your can take photo")

s=samsumg()
s.call()
s.color()
s.photo()

print(issubclass(samsumg,phone))