启动 bash /root/start.sh&&/etc/init.d/ssh restart&&sleep infinity


cat file
ls ll
cp fileprefix* newdir
mv file dir
mv oldfile newfile
--xxx=
netstat -tunlp|grep PORT
netstat -anp | grep 15148 得到PID
ps -aux | grep jupyter
kill -9 pid
touch 
which
mkdir
rm -r   可以删除有文件的目录。
rm 不能删除目录。
which python

service xxx start

export VAR=xxx
echo $VAR

cp --recursive

su ./xxx.sh param

chmod 777 file

cmd &
# comment
>> xx.log

nvidia-smi
nvcc -V
cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2  cudnn版本号

conda create -n [your_env_name（你的虚拟环境的名字）] python==[X.X]（2.5、3.8等)
conda install cudnn==8.2.1
conda activate 
conda list
conda info
conda env list