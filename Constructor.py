class student:
        roll=""
        gpa=""

        def __init__(self,roll,gpa):
                self.roll=roll
                self.gpa=gpa
        
        def display(self):
                print(f"Roll: {self.roll}, GPA: {self.gpa}")

Rahim=student(101,3.5)
Rahim.display()

Arifen=student(5284,3.55)
Arifen.display()

