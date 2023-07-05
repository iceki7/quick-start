vs里安装cmake/c++相关组件。
建个cpp程序跑一下，会自动提醒缺少的组件。


clone phy/phy
git submodule init
git submodule update

建一个build目录
cmake config,generate。如果变红，就config两次。
如果失败清理cmake cache
设置启动项目为sample模块

# 方法对校园项目无效。

