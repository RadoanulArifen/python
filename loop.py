i=10
while i>=2:
    print(i)
    i-=1

n=int(input('Enter your number: '))
i=1
while i<=10:
    print(n*i)
    i+=1

num=(1,4,9,16,25,36,49,50,74)
x=int(input('Enter your num: '))
i=0
while i<len(num):
    if x==num[i]:
        print("found",i)    
    else:
        print('Not found')
    i+=1

      
input_num=int(input())
formatted_num="{:,}".format(input_num)
print(formatted_num)

input_number =int(input("number: "))
formatted_number = ("{:,}".format(input_number))
print(formatted_number)