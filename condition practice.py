num=int(input("Enter your number: "))

if(num%2==0):
    print("Even")
else:
   print("odd")


a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
c=int(input("Enter your third number: "))

if(a>b and a>c):
    print("A is big")

elif(b>a and b>c ):
    print("B is big")
else:
    print("C is big")