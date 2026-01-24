# a = input("Enter your name: ")
# b = "Good morning,{}. How are you".format(a)
# print(b)

#CEILING FUNCTION
import math
a = 4.5
b = math.ceil(a)
print(b)

#FLOOR FUNCTION
import math
a = 4.5
b = math.floor(a)
print(b)

#ROUND FUNCTION
import math
a = 4.5
b = round(a)
print(b)


# a = input("Enter your name: ?")
# if a=="Anik":
#     print("I am going to school")
# elif a=="Anika":
#     print("I am going to college")
# else:
#     print("I am going to home")

# Fruits = "Apple"
# a = list(Fruits)
# a.append("Kiwi")
# print(a)

# for i in range(1, 11):
#     print(i)

# for i in range(1, 11,2):
#     print(i)

a = [1,2,3,4,5,"c",6,7,8,9,10]
for i in a:
    if i == "c":
        continue
    print(i)
else:
    print("Loop completed")

from collections import Counter
a = [1,2,3,3,3,2,9,98]
result = Counter(a)

print(result)

a = [1,2,3,3,3,2,9,98]
freq = {}

for i in a:
    freq[i] = freq.get(i, 0) + 1

print(freq)
