import numpy as np

row1=np.linspace(1,30,3,dtype='int')
row3=np.linspace(1,30,3,dtype='int')
row2=np.random.randint(1,30,3,dtype='int')
row4=np.random.randint(1,30,3,dtype='int')

matrix=np.array([row1,row3,row2,row4])
print(matrix)
diagonal_value=np.diagonal(matrix)
print(diagonal_value)
print(diagonal_value.shape)
above_diagonal_value=matrix[0,]
print(above_diagonal_value)

reshape=matrix.reshape(3,4)
print(reshape)

mean=np.mean(reshape[:,1:],axis=0)
print(mean)
max=np.max(reshape[:,1:],axis=0)
print(max)
varience=np.var(reshape[:,1:],axis=0)
print(varience)
std=np.std(reshape[:,1:],axis=0)
print(std)
sum=np.sum(reshape[:,1:],axis=0)
print(sum)