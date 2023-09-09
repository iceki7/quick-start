import numpy as np
import time

import matplotlib.pyplot as plt

#import dir.file
#from pythonfilename import 

#import torch
# print(torch.__version__)
# print(torch.version.cuda)
# print(torch.backends.cudnn.version())

#import tensorflow as tf
#tf.__version__ 
#print(tf.test.is_gpu_available())

import os
import sys
print("[Version]   "+sys.version)#E
print("[Executable]   "+sys.executable)#E
print("[currentPath]   "+os.getcwd())  #current path
os.chdir("/home/yanzhexi/PyTorch-VAE" )
sys.path.append(".")# NOT write to DISK
sys.path.append('./pkg1') #./表示相对路径
print(sys.path)
#sys.exit()
sys.getsizeof(var1)





  


  

# prm---------
mid="123" #model id
dsnm='test00000001.npy'
epo=1000







#mat
import scipy.io as sio
if(bloadmodel==False):
    filepath = './result/mat/'
    filename = (tid+'.mat') 
    sio.savemat(os.path.join(filepath, filename), {'xmesh':xmesh})
    print('mat SAVED')


#syntax
assert([3,5]==[3,5])
print(type(a))#a.shape
a=1+\
2
b=[1,3,\
5]

print(7/3)
print(7//3)
math.isnan()
print(r'5\n\n3')#去除转义
for k in range(5,9):#[)
    print(k)

print("hello %.2f"%3.1415)
m=np.prod([i+1 for i in [1,2,3,4]])
print(m)


# k[k==k] # nan
k=(c/b)[np.isfinite(c/b)]

#array process
allvel=np.concatenate((all_data_u,all_data_v,all_data_w),-1)# 把最后一维拼起来
allvel=np.swapaxes(allvel,0,4)#交换对应的两个维度
arr=arr.astype(np.float64) #float32=float ,float64=double
a = np.array([1])
zzz=np.zeros((sizD[0],sizD[1],sizD[2],sizT),dtype=np.float32)
b=np.ndarray([7])
b=np.array([3,5,1])
tt=np.random.choice(10, num, replace=False)# get from 0~9 and NO REPEAT
print(np.random.randn(2,3))
a=a.flatten()

#filter
print(k[k<0.3])
b=b.T
# .ravel
# .reshape(ar,[W,L])

[dudx,dudy,dudz]=np.gradient(velu)#velu.shape=(3,3,3)


#随机抽取子集
def tvset(ds,ratio=0.2):#validate ratio
    dsnum=len(ds)
    vnum=int(dsnum*ratio)
    idxl = np.arange(0, dsnum) 
    np.random.shuffle(idxl) # 打乱数组的顺序

    vidxl = idxl[:int(vnum)] 
    print(vidxl)#即测试序号

    mask = np.ones(len(ds), bool)
    mask[vidxl] = False

    dst = ds[mask]#train
    dsv = ds[vidxl]#validate
    
    return dst,dsv


#copy and delete
if 'oria' in globals():# if defined
    del oria #释放GPU内存
b2=copy.copy(b)
b2[1]=5
print(b[1])



#time
time.process_time()
time.time()#1970 secs
time.sleep()#sec



# ax3.set_facecolor('#000000') 
# ax3.plot_surface(X, Y, ar, cmap='viridis')  # 模糊一点

#3D
# plt.gca().view_init(30, -30)    默认是30和-60
# plt.gca().dist=7 #默认是10

#torch
#outputs=model(input) model()间接调用了forward方法
#.permute(2, 3, 4, 0,1)交换维度顺序
#input_data.detach().cpu().numpy()




res=[]
res.append(tid)
res.append("L2 = "+str(0.25))
def fres():
    for x in res:
         print(x)



# plot
plt.plot(epochs, loss_values, label='Training Loss')  # 曲线。range,list
plt.title('Training Loss')
plt.xlabel('Epochs')
plt.axes(yscale="log")
plt.grid(True, linestyle="--", alpha=0.5)
plt.ylim(bottom=0, top=1)
plt.imshow(oriu.astype(np.float32))#矩阵转热力图
plt.axis('off')
plt.subplot(2, 2, 1)#几行几列第几副图
plt.imshow(resu.astype(np.float32))
plt.tight_layout()
plt.legend() # 显示图例
#show之前save
plt.savefig('./results/'+tid+frameId+'-A.png',bbox_inches='tight',pad_inches=0.0, dpi=300)
plt.show()

#ax
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_trisurf(verts[:, 0], verts[:,1], faces, verts[:, 2],
#                 cmap='Spectral')#lw=1
# ax.set_xlim3d(-1.55, 0)
# ax.set_ylim3d(1, 4.5)
# ax.set_zlim3d(-3, 0)
# # ax.set_xlim3d(-1.2, 3.9)
# # ax.set_ylim3d(-1, 1)
# # ax.set_zlim3d(0, 2)
# plt.gca().view_init(30, -30)
# #plt.zlim(0,2)
# plt.show()


# 曲面
x = np.linspace(0,2,5)#左闭右闭
y = np.linspace(0,2,7)
xv,yv = np.meshgrid(x,y)
print(xv.shape)





#Relative l2
    # l2= ||u-u' ||_2 /  || u ||_2 
delta=inp - outp
l2=np.linalg.norm(delta)/ np.linalg.norm(oriu0)
# norm：take the matrix as a vector and calc its norm

#mse
np.mean(np.square(delta))


#Normal noise
input_var = np.var(oriu0)
coef=0.05
mean = 0
var = 0.1 #default 0.1 zparam
var = 1#0.005
sigma = var ** 0.5
noise = np.random.normal(mean, sigma, (velafloat.shape[1], velafloat.shape[2]))
noise = coef*noise.reshape(velafloat.shape[1], velafloat.shape[2])
velafloat[i,:,:,0]+=noise
        

# Add Gauss Noise
#     u_train = u_train + noise*np.std(u_train)*np.random.randn(u_train.shape[0], u_train.shape[1])
#     v_train = v_train + noise*np.std(v_train)*np.random.randn(v_train.shape[0], v_train.shape[1])    



# 坐标序列化。随机在一个时空域内取点，然后得到它们的坐标
allnum=velall.shape[0]*velall.shape[1]*velall.shape[2]
idx = np.random.choice(allnum, samplenum, replace=False)#所选取的点的序号
m=np.vstack(np.unravel_index(idx, (velall.shape[0], velall.shape[1], velall.shape[2]))).T#所选取的点的坐标
tt=m[:,0]
xx=m[:,1]
yy=m[:,2]