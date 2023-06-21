import os

import sys
import numpy as np
import time
#import torch
# print(torch.__version__)
# print(torch.version.cuda)
# print(torch.backends.cudnn.version())

#import tensorflow as tf
#tf.__version__ 



a = np.array([1])
print(type(a))
np.save("test00000001",arr=a)# np.array or list
data = np.load('test00000001.npy')



print("[Version]  👉 "+sys.version)#E
print("[Executable]  👉 "+sys.executable)#E
print("[currentPath]  👉 "+os.getcwd())  #current path
#print(tf.test.is_gpu_available())


time.process_time()

for i in range(0,3):
    print(i)
a=1+\
2

b=[1,3,\
5]
b=np.ndarray([7])
b=np.array([3,5,1])
# print('a')
# print(b.shape)
# print(b)
# b=np.array([b])
# b=b.T
# print('b')
# print(b.shape)
# print(b)


a=np.array([[2,5],[1,3]])
b=np.array([7,10,9,0])
c=np.array([1,2,3,4.5])
d=np.array([-1,-2,-3,-4.5])

print(c/b)
k=(c/b)[np.isfinite(c/b)]
k=k[k<0.3]

print(k)
print(abs(d))
print(type(b))
a=a.flatten()
print(np.mean(c**2))
print(d.size)

# np.array
# .shape
# .ravel
# .reshape(ar,[W,L])
# .meshgrid
# k=k[k==k]
# plt.xlim
# ax3.set_facecolor('#000000') 
# ax3.plot_surface(X, Y, ar, cmap='viridis')  # 模糊一点
# plt.gca().view_init(30, -30)    #默认是30和-60
# plt.gca().dist=7 #默认是10
# plt.axis('off')
# plt.show()
# fig.savefig(output_path,dpi=800,bbox_inches='tight')

# print('linspace')
# print (np.linspace(0,2,6))
nx,ny = (2,5)
x = np.linspace(0,2,nx)
y = np.linspace(0,2,ny)
print(x)
print(y)
xv,yv = np.meshgrid(x,y)
print(xv.ravel())
# #[ 0.  1.  2.  0.  1.  2.  0.  1.  2.]
print(yv.ravel())
# #[ 0.  0.  0.  1.  1.  1.  2.  2.  2.

print('👇')
for k in range(5,9):#起始值/终值。含起始值
    print(k)

# print(7//3)