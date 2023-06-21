
tf 1.15 在RTX3090上跑起来会卡住。无法开始训练。
可能是cudnn版本的问题。tf1.15，cudnn，rtx3090不适配。

解决：直接删掉cudnn文件：

cd /usr/local/cuda/include/ 
rm -r cudnn.h
cd /usr/local/cuda/lib64/ 
rm -r libcudnn*


检查mapping里已经没有3090：

    Device mapping:
    /job:localhost/replica:0/task:0/device:XLA_CPU:0 -> device: XLA_CPU device
    /job:localhost/replica:0/task:0/device:XLA_GPU:0 -> device: XLA_GPU device
