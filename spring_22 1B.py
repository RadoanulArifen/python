semester_fee=int(input("Enter your semester fee: "))
your_result=float(input("Enter your result: "))

if your_result>3.50:
    waiver_percent=20
elif 3.00 <= your_result >=3.50:
    waiver_percent=10
else:
    waiver_percent=5

waiver_amount=(waiver_percent/100)*semester_fee
print("net waiver amount is: ",waiver_amount)