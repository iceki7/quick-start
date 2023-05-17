load xx.mat;
J=1;
A=reshape(pos2,[8200,3]);%reshape总是先把同一列的元素合并。先同一行合并需要使用转置T''
[r,c]=size(A);
del=[]
for i=1:r 	#1和r都能取到
	tpos=A(i,:);
	if 
		del=[del i];
	elseif abs(tpos(3))<=... &&  ......
		......
	end
end
A(del,:)=[];
seq(min,step,max)

%变量输出的时候是什么名字就是什么名字，跟文件名无关
