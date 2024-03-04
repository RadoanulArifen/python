class phone:
    def __init__(self):
        print("I am in phone class")


class samsumg(phone):
    
    def __init__(self):
        super().__init__()
        print("I m in smasumg class")


s=samsumg()

