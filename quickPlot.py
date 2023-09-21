import matplotlib.pyplot as plt
plt.figure()
plt.axes(yscale="log")
plt.ylim(1e-6, 1e2)
N1 = np.arange(0,len(H1.history['loss']))
N2 = np.arange(0,len(H2.history['loss']))
N3 = np.arange(0,len(H3.history['loss']))
plt.plot(N1,H1.history['loss'],label='swish')
plt.plot(N2,H2.history['loss'],label='sigmoid')
plt.plot(N3,H3.history['loss'],label='tanh')
#plt.scatter(N,H.history['loss'])
plt.title('Training Loss')
plt.xlabel('Epoch #')
plt.ylabel('Loss')
plt.grid(linestyle='-.')
plt.legend(loc=1)
    

#section 2
umin = np.min(u_data)
plt.figure()
ax1 = plt.subplot(2,3,1)
ax2 = plt.subplot(2,3,2)
ax3 = plt.subplot(2,3,3)

#zxc xmesh:64*64    u_data:64*64*64
p1 = ax1.pcolor(xmesh,ymesh,u_data[:,:,dd],cmap='RdYlGn_r', 
                shading='auto', vmin=umin, vmax=umax)
ax1.set_title(r'$u_{ori}$',fontsize=12,color='r')
ax1.axis('equal')
p2 = ax2.pcolor(xmesh,ymesh,v_data[:,:,dd],cmap='RdYlGn_r', 
                shading='auto', vmin=vmin, vmax=vmax)
ax2.set_title(r'$v_{ori}$',fontsize=12,color='r')
ax2.axis('equal') 


plt.colorbar(p1, ax=ax1)
plt.colorbar(p2, ax=ax2)

ax4 = plt.subplot(2,3,4)
ax5 = plt.subplot(2,3,5)
ax6 = plt.subplot(2,3,6)
p4 = ax4.pcolor(xmesh,ymesh,all_data_u[:,:,dd],cmap='RdYlGn_r', 
                shading='auto', vmin=umin, vmax=umax)
ax4.set_title(r'$u_{pre}$',fontsize=12,color='r')
   
plt.colorbar(p4, ax=ax4)

plt.savefig('./predict_results/Flow2D_compare.png', dpi=300)
plt.show()

#####################################3

import numpy as np
import matplotlib.pyplot as plt

# 定义x、y、z的取值范围
x = np.linspace(-5, 5, 100)    #起始/结束/点的数量，包括起始和结束
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 计算z的值
Z = X + Y

# 绘制热力图
plt.imshow(Z, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('热力图')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
######################################