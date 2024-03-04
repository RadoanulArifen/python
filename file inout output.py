with open ("practice","r") as f:
    data=f.read()

new_data= data.replace("python","Java")
print(new_data)
with open("practice","w") as f:
    f.write(new_data)

word="learning"

with open ("practice","r") as f:
    data=f.read()
    if (data.find(word)!=-1):
        print("found")
    else:
        print("not found")



