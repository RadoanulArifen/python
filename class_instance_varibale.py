class Animal:
    tiger="Tiger is a animal" #class variable
    
    def __init__(self,bird):
        self.bird=bird #instance varibale

ani=Animal("Parrot")
print(ani.bird)
print(ani.tiger)

print("\n")
ani2=Animal("Kobutor")
ani2.tiger="This is a another tiger"
print(ani2.bird)
print(ani2.tiger)
