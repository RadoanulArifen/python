class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def display_details(self):
        
        print(f"Dog's Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")

    def is_puppy(self):
        
        return self.age < 1
    
Dog1=Dog("Tommy","Mixed breed",0.5)
Dog1.display_details()
print(f"Is {Dog1.name} a puppy?\n {'Yes' if Dog1.is_puppy() else 'No'}")


