
# deploy

勾选TTY
挂载volume
设置显卡
publish a new network port


# 上网


export http_proxy=http://router4.ustb-ai3d.cn:3128
export https_proxy=http://router4.ustb-ai3d.cn:3128



#
本地映射


启动容器的时候配置端口映射：22转portainer dashboard端口。
apt install openssh-server

host:50000~65535  ->   container:  22(ssh)

设置ssh允许root登录：
sed -i 's/^PermitRootLogin/#PermitRootLogin/g' /etc/ssh/sshd_config && sed -i '$aPermitRootLogin yes' /etc/ssh/sshd_config
启动ssh。
设置密码：passwd
使用portainer dashboard IP+端口号。登录。

如果在校外需要再次调整ip。

