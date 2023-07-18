

df -h
cat file
ls ll -h
cp -r fileprefix* file/newdir 
mv -r file/dir dir
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
whereis

service ssh start

wget dir url

jupyter server list

export VAR=xxx
echo $VAR
unset VAR

cp --recursive

su ./xxx.sh param

chmod 777 file

cmd &
# comment
>> xx.log

nvidia-smi
nvcc -V
cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2  cudnn版本号

conda deactivate
conda create -n [your_env_name（你的虚拟环境的名字）] python==[X.X]（2.5、3.8等)
conda install cudnn==8.2.1
conda activate 
conda list
conda info
conda env list
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn
conda config --show channels
& #后台执行
&& #先执行的必须成功再执行后一个命令


#查看端口
ss -lntup
lsof -i
netstat


apt update 
apt-get update
apt install
apt-get install -y #不一样


nohup xxx & #与终端无关，且后台执行
tail -f nohup.out #查看文档末尾，并实时同步



ssh -p xxxx root@ip #win