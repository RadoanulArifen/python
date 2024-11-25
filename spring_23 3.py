def list_to_dict(key,value):
    return {k:v for k,v in zip(key,value)}
K = [1001, 1002, 1003, 1004, 1005]
V = ["USA", "Canada", "China", "Japan", "UK"]
result_dict=list_to_dict(K,V)
print(result_dict)


def list_to_dic(key,value):
    return{x:y for x,y in zip(key,value)}
X = [1005, 1006, 1007, 1008, 1009]
Y = ["USA", "Canada", "China", "Japan", "UK"]
result_dic=list_to_dic(X,Y)
print(result_dic)