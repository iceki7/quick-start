
#experiment basic---------
torch.manual_seed(1234)
np.random.seed(1234)    #保证结果唯一性
random.seed(1234)
#为了允许重复执行单个cell ，可在每次调用函数前再单独设置。




bloadmodel=0    #swi
btrain=1
bsavemodel=1    #如果加载了模型，会覆盖原模型的参数

tid=str(int(time.time()))
if(bloadmodel):
    tid=123
    tid=str(tid)   #prm
print('tid  '+tid)

"""
步骤：
1.准备tid，锁定随机性
2.划分路径
3.存档
    Loss数组
    保存torch模型（不仅仅是保存参数而是保存模型，之后导入时先引入模型的类即可）
4.标注:
    #prm
    #hyp 一般不需要调节的参数
    #res 结果
    #inf 代码中的关键信息
    #chg 对代码做出的修改
    #add 增加的func
    #swi  做对比实验的时候常用
    #cri =criterion
5.小epoch试跑
6. 能用变量名表示的就不要用数字。否则更换参数时困难
"""


aloss=[]

if(bloadmodel):
    #loadmodel

    #loadloss
    aloss = np.load("/res/loss-"+tid+".npy",allow_pickle=True)
    aloss=aloss.tolist()
    print('done')

if(train):
    stm=time.time()#1970 secs
    
    for:
        aloss.append(loss)

    etm=time.time()
    print('train time(s)\t'+str(etm-stm))
    
    err=(v-v0)/v0*100
    print('relative error\t'+str(err)+'%')

if(bsavemodel):
    #savemodel

    #saveloss
    np.save("/res/loss-"+tid,arr=aloss)# np.array or list
    print('done')

def pltCurve(x,y):
    plt.plot(x, y, label='Training Loss')
    plt.show()