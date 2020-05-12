N=int(input())
men=[]
count=[]
accept=[]
index=[]
men_pre=[]
te=[]
for i in range(N):
    men.append(list(map(int,input().split(' '))))
    count.append(0)
    accept.append(0)
    index.append(0)
    men_pre.append(0)
    te.append(0)
women=[]
for i in range(N):
    women.append(list(map(int,input().split(' '))))
q=int(input())
qu=[]
for i in range(q):
    qu.append(int(input()))
sum_a=sum(accept)
i=0
while(sum_a<N):
    i=0
    while(i<N):
        if men_pre[i]==0:
            pre=min(men[i])
            inx=men[i].index(pre)
            if accept[inx]==0:
                count[inx]=count[inx]+1
                accept[inx]=1
                index[inx]=[women[i][inx],i]
                men_pre[i]=1
                men[i][inx]=20
                i=i+1
            elif accept[inx]==1 and (women[i][inx]<=index[inx][0]):
                count[inx]=count[inx]+1
                k=index[inx][1]
                index[inx]=[women[i][inx],i]
                men_pre[i]=1
                #print(index[inx][1])
                men_pre[k]=0
                men[i][inx]=20
                i=i+1
            elif accept[inx]==1 and (women[i][inx]>index[inx][0]):
                count[inx]=count[inx]+1
                men[i][inx]=20

        else:
            i=i+1
    sum_a=sum(accept)

for i in range(q):
    print(count[(qu[i])-1])
    