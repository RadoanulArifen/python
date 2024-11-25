list1_str=input("input for list 1: ")
list1=list1_str.split()

list2_str=input("Input for list 2: ")
list2=list2_str.split()

common_list=[]

for element in list1:
    if element in list2:
        common_list.append(element)
print(common_list)
