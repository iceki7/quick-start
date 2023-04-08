import os

import sys
import numpy as np

print("[Version]  👉 "+sys.version)#E
print("[Executable]  👉 "+sys.executable)#E
print("[currentPath]  👉 "+os.getcwd())  #current path
#print(tf.test.is_gpu_available())

a=1+\
2

b=[1,3,\
5]
b=np.ndarray([7])
b=np.array([3,5,1])
print('a')
print(b.shape)
print(b)
b=np.array([b])
b=b.T
print('b')
print(b.shape)
print(b)


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