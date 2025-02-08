def mul_table(n):
    for i in range(1,11):
        print("{}*{}={}".format(n,i,n*i))




n=int(input("enter the number: "))

while n!=0:
    mul_table(n)
    print("")
    n=int(input("enter the number: "))
    
