
import numpy as np
list_array=list(range(100))
array=np.array(list_array)

shape_change=array.reshape(10,10)
print(shape_change)

sum=np.sum(shape_change[:,0:,],axis=0)
print(sum)

