df -h
du -sh *



cat file
ll -h
ls -lhd
ls | grep 
date

cp -ri 
#fileprefix* file/newdir 


#执行第一个命令成功后再执行第二个
cp v1 v2 &&
echo 123123


# 批量移动：
find . -maxdepth 1   -type f -name "*.h5*" -exec mv {} /workspace/DeepLagrangianFluids-FORK/scripts  \;
# 文件名不要包含[


mv -i 
#oldfile newfile
#file/dir dir

--xxx=
netstat -tunlp|grep PORT
netstat -anp | grep 15148 得到PID

ps -aux | grep 
# +process name
# 第二个参数是pid

kill -9 
# +pid

touch 
which
mkdir

git status 
# 工作区

git checkout -- 
#filename 放弃更改



rm -r   可以删除有文件的目录。
rm 不能删除目录。
rm *

rm -r *
#*name* 含name的
# name* name开头的


which python
whereis

端口占用
netstat -plnt 

apt-get update 
# 信息更新
apt-get upgrade 
# 会下载
apt-get install 


SSH配置
vi /etc/ssh/sshd_config
grep Port /etc/ssh/sshd_config
service ssh start
service ssh restart
service ssh status
ssh -p 50002 root@srouter6.ustb-ai3d.cn
exit


passwd
pwd

wget dir url

curl www.baidu.com	联网测试

jupyter server list

export VAR=
echo $VAR
unset VAR

cp --recursive

su ./xxx.sh param

chmod 777 file

./exe args

cmd &
# comment
>> xx.log

nvidia-smi
nvcc -V
cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2  cudnn版本号


./run_network.py --weights pretrained_model_weights.h5 \
                 --scene example_scene.json \


find / -name 'libnvidia-ml*'


tmux
ctrl b d
ctrl b : set mouse on
tmux ls 
tmux attach -t 0
tmux kill-session -t0
32.6609

unzip -q 
# 不输出解压信息

zip -rq 
# dir.zip dir



ctrl c


echo a{3..10}b

shell变量名后面不要跟_  比如$var1_ 

md5sum 

