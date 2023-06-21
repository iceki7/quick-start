import numpy as np
# print(np.reshape([1,2,3,4],np.array([[5,6],[7,8]]).shape))

x=np.array([[1,2],[4,7],[5,9]])
print(x.max(0))

a=np.array([7,5,2,9,6,6])
b=np.array([1,3])
print(np.setdiff1d(a,b))
print(np.array([np.delete(a,b)]).T.shape)

#12
#57
#49