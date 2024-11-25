import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])

print(matrix)

diagonal=np.diag(matrix)
print(diagonal)

above_diagonal=np.diag(matrix,k=1)
print(above_diagonal)

below_diagonal=np.diag(matrix,k=-1)
print(below_diagonal)

matrix_3x4=matrix[:,:3].T
print(matrix_3x4)

mean=np.mean(matrix_3x4[:, 1:],axis=0)
max_val=np.max(matrix_3x4[:, 1:],axis=0)
variance=np.var(matrix_3x4[:, 1:],axis=0)
print(mean)
print(max_val)
print(variance)