N=int(input())
a=[]
flag=[]
f=0
for i in range(N):
    a.append(list(map(int,input().split(' '))))
    flag.append(0)
flag.append(0)
for i in range(1,N+1):
    f=0
    for j in range(N):
        if i  not in a[j]:
            f=f+1

    if f==len(a):
        flag[i]=1
    
count=0
for i in range(N+1):
    if flag[i]==1:
        print(i)
        count=count+1
if count==0:
    print(-1)
    