class student:
        roll=""
        gpa=""

        def set_value(self,roll,gpa):
                self.roll=roll
                self.gpa=gpa
        
        def display(self):
                print(f"Roll: {self.roll}, GPA: {self.gpa}")

Rahim=student()
Rahim.set_value(101,3.5)
Rahim.display()

Arifen=student()
Arifen.set_value(5284,3.36)
Arifen.display()

