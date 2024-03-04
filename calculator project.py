def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply (x,y):
    return x*y

def divids(x,y):
    if y!=0:
        return x/y
    else:
        return "Error"
def squre(x):
    return x**x

import math
def root(x):
    return math.sqrt(x)

def prime(x):
    for i in range(2,int(x/2)):
        if(x%i==0):
            return " Not a prime "
        
    return "Prime"

import math
def factorial(x):
    return math.factorial(x)


def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)

    
while True:
    print("\nOptions: ")
    print("1. Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Squre any value")
    print("6.Find Root for any positive number")
    print("7.check prime number")
    print("8.Check Factorial")
    print("9.Check Fibonacci")
    print("10.Exite from calculator")

    Choice=input("Enter your choice (1-10): ")

    if Choice=="1":
        num1=float(input("Enter your frist number: "))
        num2=float(input("Enter your second number: "))
        result=add(num1,num2)
        print(f"Result: {result}")

    elif Choice=="2":
        num1=float(input("Enter your frist number: "))
        num2=float(input("Enter your second number: "))
        result=subtract(num1,num2)
        print(f"Result:{result}")
    
    elif Choice=="3":
        num1=float(input("Enter your frist number: "))
        num2=float(input("Enter your second number: "))
        result=multiply(num1,num2)
        print(f"Result:{result}")

    elif Choice=="4":
        num1=float(input("Enter your frist number: "))
        num2=float(input("Enter your second number: "))
        result=divids(num1,num2)
        print(f"Result:{result}")

    elif Choice=="5":
        num1=int(input("Enter your number: "))
        result=squre(num1)
        print(f"Result:{result}")
    
    elif Choice=="6":
        num1=float(input("Enter your number: "))
        result=math.sqrt(num1)
        print(f"Result:{result}")

    elif Choice=="7":
        num1=int(input("Enter the number: "))
        result=prime(num1)
        print(f"Result:{result}") 

    elif Choice=="8":
        num1=int(input("Enter the number: "))
        result=math.factorial(num1)
        print(f"Result:{result}")

    elif Choice=="9":
        num1=int(input("Enter the number: "))
        result=fibonacci(num1)
        print(f"Result:{result}")    

    elif Choice=="10":
        print("Exiting from the calculator!!")
        break
    else:
        print("Please enter the number (1-10)...Thankyou!!")
