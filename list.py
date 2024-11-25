list=[]

for number in range(20,61):
    if number%2==0:
       num= number+5
       list.append(num)

        
    elif number%5==0:
       num= number+2
       list.append(num)

       
print(list)
