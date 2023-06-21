#!/bin/bash

dir=/sitonholy

#VSCODE_PORT=8888
#VSCODE_PASSWORD=123456
#JUPYTER_PORT=8888
#JUPYTER_PASSWORD=Scm123456

web_vscode() {
if [ ! -d $dir/vscode ]; then
  mkdir -p $dir/vscode
fi
cat > $dir/vscode/config.yaml << EOF
bind-addr: 0.0.0.0:$VSCODE_PORT
auth: password
password: '$VSCODE_PASSWD'
cert: false
EOF

code-server --config=$dir/vscode/config.yaml  &> $dir/log/web-vscode.log  &
echo "start vscode"
}

web_vscode_env() {
if [ -z  $VSCODE_PORT ];then
        echo "no vscode port"
elif [ -z $VSCODE_PASSWD ];then
        echo "no vscode password"
else
        web_vscode
fi
}

jupyter_lab() {
if [ ! -d $dir/jupyter ]; then
  mkdir -p $dir/jupyter
fi
cat > $dir/jupyter/jupyter_lab_config.py << EOF
c.ServerApp.ip = '0.0.0.0'
c.ServerApp.port = $JUPYTER_PORT
c.ServerApp.token = '$JUPYTER_PASSWD'
c.NotebookApp.open_browser = False
c.NotebookApp.terminado_settings = {'shell_command' : ['/bin/bash']}

import os
c.ServerApp.root_dir = "/root"
c.MultiKernelManager.default_kernel_name = 'python3'
c.NotebookNotary.db_file = ':memory:'
c.ServerApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors * 'self' "
    }
}

c.NotebookApp.allow_remote_access = True
c.NotebookApp.iopub_data_rate_limit = 1000000.0
c.NotebookApp.rate_limit_window = 3.0
EOF

jupyter-lab --allow-root --config=$dir/jupyter/jupyter_lab_config.py  &> $dir/log/jupyter.log  &
echo "start jupyter"
}

jupyter_env() {
if [ -z  $JUPYTER_PORT ];then
        echo "no jupyter port"
elif [ -z $JUPYTER_PASSWD ];then
        echo "no jupyter password"
else
        jupyter_lab
fi
}

# tensorboard
run_tensorboard() {
tensorboard --logdir=$TENSORBOARD_PATH --bind_all --port=$TENSORBOARD_PORT  &> $dir/log/tensorboard.log  &
echo "start tensorboard"
}


tensorboard_env() {
if [ -z  $TENSORBOARD_PORT ];then
        echo "no tensorboard port"
elif [ -z $TENSORBOARD_PATH ];then
        echo "no tensorboard path"
else
        run_tensorboard
fi
}

# novnc
run_novnc() {
# run novnc
rm -rf /tmp/.X1*

# run vnc
vncpasswd <<!
$VNC_PASSWD
$VNC_PASSWD
!

vncserver :1 -localhost no -geometry=1920x1080
bash /sitonholy/sitonvnc/utils/launch.sh --listen $VNC_PORT --vnc 127.0.0.1:5901 &> $dir/log/novnc.log  &

echo "start tensorboard"
}

novnc_env() {
if [ -z  $VNC_PASSWD ];then
        echo "no vnc passwd"
elif [ -z $VNC_PORT ];then
        echo "no vnc port"
else
        run_novnc
fi
}


if [ ! -d $dir/log ]; then
  mkdir -p $dir/log
fi

# run 
# web_vscode_env
jupyter_env
tensorboard_env
# novnc_env
