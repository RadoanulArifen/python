import numpy as np

a=np.array([1,2,3]) #1d array vector
print(a)
print(type(a))
print(a.shape)
print(a.ndim)
print(a.dtype)

twod=np.array([[1,2,3],[4,5,6]]) #2d array
print(twod)
print(twod.shape)
print(twod.ndim)
print(twod.dtype)

threed=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(threed)
print(threed.shape)
print(threed.size)
print(threed.ndim)
print(threed.dtype)
print(threed.nbytes)

zeros=np.zeros((2,2),dtype='float')
print(zeros)

zeros1=np.zeros((3,3),dtype='int')
print(zeros1)

ones=np.ones((2,2),dtype='int')
print(ones)

full=np.full((2,3),5,dtype='int')
print(full)

arange=np.arange(1,10,2)
print(arange)

linspace=np.linspace(1,100,50,dtype='int')
print(linspace)

linspace1=np.linspace(2,100,50,dtype='int')
print(linspace1)


#..................................................Array indexing and slicing........................................................


#.................Indexig....................

array=np.array([1,2,3,4,5])
print(array)

print(array[1])
print(array[-3])

#random array
rarray=np.random.randint(1,10,size=(3,3))
print(rarray)
print(rarray[1,1])
print(rarray[2,0])


rarray1=np.random.randint(1,10,size=(2,3,3))
print(rarray1)
print(rarray1[0,1,1])
print(rarray1[1,1,2])



#.............................SLICING.........................
array5=np.array([1,2,3,4,5])
print(array5)
print(array5[0:3])
print(array5[2:])
print(array5[2:-2])


rarray=np.random.randint(1,10,size=(3,3))
print(rarray)
print(rarray[1:,1:])



#.............RESHAPE..............................

reshape=np.array([[1,2,3,4],[5,6,7,8]])
print(reshape)
print(reshape.size)
print(reshape.shape)
print(np.reshape(reshape,(4,2)))

#.................dip copy shallow copy.........................
arr=np.array([1,2,3,4,5])
cp=arr.copy()
cp[2]=5
print(cp)
print(arr)
print(id(arr))
print(id(cp))


