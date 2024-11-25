class phone:
    def __init__(self):
        print("I am in phone class")


class samsumg(phone):
    
    def __init__(self):
        super().__init__()
        print("I m in smasumg class")


s=samsumg()



class Human:
    def __init__(self):
        print("I have 2 eyes")

    def eat(self):
        print("I can eat")
    
    def drink(self):
        print("I can drink")
    
class Male(Human):
    def drink(self):
        super().drink()
        print("I can drink tea")
    def __init__(self):
        super().__init__()
        print("I have 1 nose")

Arifen=Male()
Arifen.eat()
Arifen.drink()

