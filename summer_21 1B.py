day_list=['Saturday','Sunday','Tuesday','Thuesday','Friday']
day_list.insert(2,'Monday')
day_list.insert(4,"Wednesday")
print(day_list)

def take_day(day):
    if day==day_list[-1]:
        print("Today is holyday")
    else:
        print("Working day")
day=input("Enter your day: ")
result=day
take_day(result)