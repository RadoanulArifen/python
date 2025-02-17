#read a file 
filename="input.txt"
fp=open(filename)
content=fp.read()
fp.close()
print(content)

#write a ile
filename="input.txt"
file=open(filename,"w")
content=file.write("this is a new writting file")
file.close()
print(content)

#write file with previous content
filename="input.txt"
file=open(filename,"a")
content=file.write("\nThis is new content with previous content\n")
file.close()
print(content)

#read file in morden rule
filename="input.txt"
with open(filename) as f:
    content=f.read()
    print(content)


filename="input.txt"
file=open(filename)
content=file.read()
file.close()
print(content)

filename="input.txt"
file=open(filename,"w")
content=file.write("jdshfbwkusgf")
file.close()
print(content)


