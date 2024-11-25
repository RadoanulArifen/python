def payment(dict,index):

    if index in dict:
        plan=dict[index]["plan"]
        if(plan=='Basic'):
            print("Starting at $9.99")
        elif(plan=='Standard'):
            print("Starting at $15.99")
        elif (plan == 'Premium'):
            print("Starting at $19.99")
    else:
        print("Index is not found")



dict= {}

size = int(input("Enter the size : "))

for x in range(size):
    dict_index= int(input("Enter the index: "))

    dict[dict_index]={}
    name=input("Enter your name : ")
    plan=input("Enter your plan : ")

    dict[dict_index]["name"]=name
    dict[dict_index]["plan"] = plan


print(dict)