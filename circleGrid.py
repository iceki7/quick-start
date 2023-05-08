#画一个圆，筛出圆内的格点的坐标
import os
import sys
import numpy as np

nx,ny = (3,4)
x = np.linspace(0,10,nx)    #起始/结束/点的数量，包括起始和结束
y = np.linspace(0,10,ny)

xv,yv = np.meshgrid(x,y) #ravel后就变成了均匀采样的坐标，xv[i],yv[i]
xv=xv.ravel()   
yv=yv.ravel()

dellist=[]
radius=8
for i in range(0,x.size*y.size):
    tx=xv[i]
    ty=yv[i]
    if(tx**2+ty**2<=radius**2):
        dellist.append(i)
xv=np.delete(xv,dellist)
yv=np.delete(xv,dellist)   #删除索引列表里的元素
