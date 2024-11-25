import numpy as np

matrix1D = np.array([1,2,3,4])

print(matrix1D)
print(matrix1D.dtype)
print(matrix1D.ndim)

matrix2D = np.array([[1,3,4],[5,6,7],[8,9,10]])
print(matrix2D)
print(matrix2D.dtype)
print(matrix2D.ndim)




#Create a two-dimensional array from a list comprehension that 
#produces the even integers from 2 through 20 in the first row and
# the odd integers from 1 through 21 in the second row.


matrixD = np.array([[x for x in range(2,21,2)],[x for x in range(1,21,2)]])
print(matrixD)
print(matrixD.size)

rarray1=np.random.randint(1,10,size=(3,3,3))
print(rarray1)
print(rarray1[2:,1:,1:])

