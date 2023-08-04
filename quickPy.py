import os
import sys
import numpy as np
import time
#import dir.file
#from pythonfilename import 

#env test
#import torch
# print(torch.__version__)
# print(torch.version.cuda)
# print(torch.backends.cudnn.version())

#import tensorflow as tf
#tf.__version__ 
#print(tf.test.is_gpu_available())

print("[Version]  👉 "+sys.version)#E
print("[Executable]  👉 "+sys.executable)#E
print("[currentPath]  👉 "+os.getcwd())  #current path
os.chdir("/home/yanzhexi/PyTorch-VAE" )
sys.path.append(".")# NOT write to DISK
#print(sys.path)
sys.path.append('./pkg1')



#basic
assert([3,5]==[3,5])

a = np.array([1])
print(type(a))#a.shape

np.save("test00000001",arr=a)# np.array or list
data = np.load('test00000001.npy')

b=np.ndarray([7])
b=np.array([3,5,1])
print(np.random.randn(2,3))
print(np.linspace(0,2,6))

print(c/b)
print(7//3)

a=1+\
2
b=[1,3,\
5]


print(k[k<0.3])


print('5\n\n3')
print(r'5\n\n3')


for k in range(5,9):#起始值/终值。含起始值
    print(k)

# k[k==k] # nan
k=(c/b)[np.isfinite(c/b)]


# print(b.shape)
# b=np.array([b])
# b=b.T
# print('b')
# print(b.shape)
# print(b)


#随机抽取子集
framenum=velall.shape[0]
testratio=0.2 #param
testnum=framenum*testratio
print(framenum)
print(testnum)
idx = np.arange(0, framenum) 
np.random.shuffle(idx) # 打乱数组的顺序
#print(idx)
idx = idx[:int(testnum)] 
print(idx.shape)#即测试帧的序号
veltest=velall[idx,:,:,:]
mask = np.ones(len(velall), bool)
mask[idx] = False
vel = velall[mask]
print(vel.shape)
print(velall.shape)


if 'oria' in globals():# if defined
    del oria #释放GPU内存
b2=copy.copy(b)

math.isnan()

time.process_time()
time.time()#1970 secs
time.sleep()#sec




print("🍎 %.2f"%3.1415)
m=np.prod([i+1 for i in [1,2,3,4]])
print(m)

a=np.array([[2,5],[1,3]])
b=np.array([7,10,9,0])
c=np.array([1,2,3,4.5])
d=np.array([-1,-2,-3,-4.5])


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


# ax3.set_facecolor('#000000') 
# ax3.plot_surface(X, Y, ar, cmap='viridis')  # 模糊一点

#3D坐标系控制
# plt.gca().view_init(30, -30)    默认是30和-60
# plt.gca().dist=7 #默认是10


plt.plot(epochs, loss_values, label='Training Loss')  # 曲线
plt.title('Training Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
#plt.axes(yscale="log")
#plt.ylim(bottom=0, top=1)
plt.imshow(oriu.astype(np.float32))#矩阵转热力图
plt.axis('off')
# plt.xlim
plt.subplot(2, 2, 1)#几行几列第几副图
plt.imshow(resu.astype(np.float32))
plt.title('res u')
plt.tight_layout()
plt.legend() # 显示图例
plt.savefig('./results/'+testid+'-'+str(imageFrame)+'-A.png',bbox_inches='tight',pad_inches=0.0, dpi=300)
plt.show()

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




# add gauss noise
#     u_train = u_train + noise*np.std(u_train)*np.random.randn(u_train.shape[0], u_train.shape[1])
#     v_train = v_train + noise*np.std(v_train)*np.random.randn(v_train.shape[0], v_train.shape[1])    

#relative l2
    # l2= ||u-u' ||_2 /  || u ||_2 
l2=np.linalg.norm(deltu)/ np.linalg.norm(oriu0)
# norm：take the matrix as a vector and calc its norm

#mse
np.mean(np.square(ypre-yori))
