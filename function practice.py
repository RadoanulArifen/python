games=["Cricket","Football","Badminton","Swimming","tenis"]

def list_count(list):
    print(len(list))

list_count(games)

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(games)



def convert_tk(usd):
    tk=usd*120
    print( tk)
    
convert_tk(2)