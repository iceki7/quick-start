
# deploy

勾选TTY
挂载volume
设置显卡
publish a new network port





# 本地映射


启动容器的时候配置端口映射：22转portainer dashboard端口。
apt install openssh-server

publish a new network port
host:50000~65535  ->   container:  22(ssh)

设置ssh允许root登录：
sed -i 's/^PermitRootLogin/#PermitRootLogin/g' /etc/ssh/sshd_config && sed -i '$aPermitRootLogin yes' /etc/ssh/sshd_config

service ssh start
passwd


使用portainer dashboard IP+host端口号。登录。

如果在校外，需要再次调整ip。
    1.转发
    2.proxifer穿透

ssh root@转发后ip -p 转发后port


# jupyter
    # 默认目录
    vi ~/.jupyter/jupyter_notebook_config.py  
    notebook_dir = 'xx'

    # 启动
    jupyter-notebook --allow-root --port=8888 --ip=0.0.0.0

jupyter notebook stop 
#接port

    
jupyter notebook list