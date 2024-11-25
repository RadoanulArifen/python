import numpy as np

arr=np.arange(0,100)
array=np.array(arr)
print(array)
new_arr=array.reshape(10,10)
print(new_arr)

print(new_arr[2:5,4:7])

parray=np.array([1,2,3,4,5,6,7,8,9])
resize=parray.reshape(3,3)
print(resize)
new_resaize=np.transpose(resize)
print(new_resaize)