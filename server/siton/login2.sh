
_read_passwd() {
    stty -echo
    trap 'stty echo' EXIT
    read "$@"
    stty echo
    trap - EXIT
    echo
}

_login() {
    read -p "请输入账号: " account

    echo -n "请输入密码: "
    _read_passwd  passwd

    curl -d "DDDDD=$account&upass=$passwd&0MKKey=123456789" "202.204.48.82"
}

_login_me() {
  curl -d "DDDDD=B1829184&upass=YAOfish123&0MKKey=123456789" "202.204.48.82"
}

_logout() {
    curl 202.204.48.82/F.htm
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
elif [ "$1" = "me" ]
then
    _login_me
elif [ "$1" = "out" ]
then
    _logout
else
    _usage
fi
