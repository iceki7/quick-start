
_read_passwd() {
    stty -echo
    trap 'stty echo' EXIT
    read "$@"
    stty echo
    trap - EXIT
    echo
}

_login() {
#     read -p "请输入账号: " account
    account=41922118
#    echo -n "请输入密码: "
    # _read_passwd  passwd
    echo "登录41922118"
    passwd=zxcv0iopW_

    curl -s -o /dev/null -d "DDDDD=$account&upass=$passwd&0MKKey=123456789" "202.204.48.66"
}

_logout() {
    curl -s -o /dev/null 202.204.48.82/F.htm
    echo "logout"
}

_usage() {
    echo "用法: "
    echo "$ ./log.sh \t[帮助]"
    echo "$ ./log.sh in \t[登录]"
    echo "$ ./log.sh out \t[注销]"
}

if [ "$#" -gt "1" ]
then
    _usage
elif [ "$1" = "in" ]
then
    _login
elif [ "$1" = "out" ]
then
    _logout
else
    _usage
fi
