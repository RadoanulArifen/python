class Student:
    roll="100"
    gpa="3.5"

rahim=Student()
rahim.roll
rahim.gpa
print(f"Roll:{rahim.roll},Gpa:{rahim.gpa}")



class apple:
    color=""
    varient=""

green_Apple= apple()
green_Apple.color="Green apple is green"
green_Apple.varient="this is a forign apple"

print(f"colour:{green_Apple.color},\nVarient:{green_Apple.varient}")


class car:
    type=""
    speed=""

v_car=car()
r_car=car()

v_car.type="This is a green car"
v_car.speed="This car speed is 200"

r_car.type="This is a red car"
r_car.speed="This car speed is 500"

print(v_car.type,v_car.speed)
print(r_car.type,r_car.speed)
