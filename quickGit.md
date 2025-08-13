暂存区，是不同的分支共享的



发布分支：创建新分支




git push origin HEAD --force

本地进度强制覆盖远程。





只要commit，就会产生一个节点
undo commit



publish branch：把分支加到远程
远程分支会有前缀origin/



merge：又会创建一个新的commit


checkout：到某个节点
位于某个节点上，和位于某个分支上，是两种不同的状态（左下角是哈希还是分支的名字）


是哈希值=在节点上="不在分支上"


PR：    xx want to merge 1 commit into branch1 from branch2




reset是将之前的提交记录全部抹去，将 HEAD 指向自己重置的提交记录；



revert      反向提交（如果是要修改一个很久之前的错误，比如中间已经被覆盖了几个节点了，reset就不合适）



tag跟着commit走。tag创建以后也要push。



【子模块】
git submodule 
    init
    update