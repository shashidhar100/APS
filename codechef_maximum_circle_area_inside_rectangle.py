Q=int(input())
res=[]
for i in range(Q):
    N=int(input())
    a=list(map(int,input().split(" ")))
    b=list(map(int,input().split(" ")))
    ma_ar=[0]*(N**2)
    for l in range(N**2):
        ma_ar[l]=((a[l//N]*b[l%N])-((min(a[l//N],b[l%N]))**2))
    vote_a=[0]*N
    vote_b=[0]*N
    sum=0
    ini=0
    fin=N-1
    for k in range(N):
        mi=min(ma_ar[ini:fin])
        inx=ma_ar.index(mi)
        q=inx//N
        re=inx%N
        while(vote_b[re]==1):
            ma_ar[inx]=10**6
            mi=min(ma_ar[ini:fin])
            inx=ma_ar.index(mi)
           
            re=inx%N
            
        re=inx%N
        vote_b[re]=1
        sum+=min(a[q],b[re])
        ini+=N
        fin+=N
    res.append(sum)
for i in range(Q):
    print(res[i])
        
        
    















    Q=int(input())
res=[]
for i in range(Q):
    N=int(input())
    a=list(map(int,input().split(" ")))
    b=list(map(int,input().split(" ")))
    vote_b=[0]*N
    ma_ar=[0]*(N)
    i=0
    sum=0
    while(i<N):
        
        for l in range(N):
            ma_ar[l]=((a[i]*b[l])-((min(a[i],b[l]))**2))
        ini=0
        fin=N
        
        mi=min(ma_ar[ini:fin])
        inx=ma_ar.index(mi)
        while(vote_b[inx]==1):
            ma_ar[inx]=10**6
            mi=min(ma_ar[ini:fin])
            inx=ma_ar.index(mi)
            
        vote_b[inx]=1
        
        sum+=min(a[i],b[inx])
        i=i+1
    res.append(sum)
for i in range(Q):
    print(res[i])
        
        
    3rd


    T=int(input())
th={'A':0,'B':1,'C':2,'D':3}
sh={'12':0,'3':1,'6':2 ,'9':3}
lis=[[0]*4 for i in range(4)]
amount=[100,75,50,25]
for i in range(T):
    su=0
    vot_th=[0]*4
    vot_sh=[0]*4
    lis=[[0]*4 for i in range(4)]
    lis_copy=[[0]*4 for i in range(4)]
    N=int(input())
    for i in range(N):
        up=list(map(str,input().split(" ")))
        lis[th[up[0]]][sh[up[1]]]+=1
        lis_copy[th[up[0]]][sh[up[1]]]+=1
    #print(lis)
    k=0
    (lis_copy[0]).sort(reverse=True)
    (lis_copy[1]).sort(reverse=True)
    (lis_copy[2]).sort(reverse=True)
    (lis_copy[3]).sort(reverse=True)
    #print(lis)
    while((max(lis_copy)!=0 and sum(max(lis_copy))!=0)):
        #print("initial",lis_copy)
        #sum_lis=[sum(lis[0]),sum(lis[1]),sum(lis[2]),sum(lis[3])]
        ma=max(lis_copy)
        #print("@@@",ma)
        inx=lis_copy.index(ma)
        #inx=lis.index(ma)
        #print("inx",inx)
        vot_th[inx]+=1
        ma=max(lis[inx])
        #print("######",ma)
        
        inx1=lis[inx].index(ma)
        #print("inx1",inx1)
        #print("vot_sh",vot_sh)
        while(vot_sh[inx1]!=0):
           ma=max(lis[inx])
           inx1=lis[inx].index(ma)
           #print("inx1",inx1)
           lis[inx][inx1]=0
           #print("lis[inx]",lis[inx])
           #print("j",j)
           #print("vot_sh",vot_sh)
           
        su=su+amount[k]*ma  
        #print("sum==",su)
        #inx1=lis[inx].index(ma)
        #print("$$$",inx1)
        vot_sh[inx1]+=1
        lis_copy[inx]=[0,0,0,0]
        k=k+1
        #print("kkkk",k)
        #print("final",lis_copy)
    if k!=4:
        dif=4-k
        su=su-(dif*100)
    print(su)
        
    
    
4th


import math
T=int(input())
for i in range(T):
    lis=list(map(int,input().split(" ")))
    n=lis[0]
    p=lis[1]
    ele=list(map(int,input().split(" ")))
    ele_copy=ele.copy()
    ele=[ele[i] for i in range(len(ele)) if p%ele[i]!=0]
    rt=p
    h=len(ele_copy)-1
    while(ele_copy[h-1]!=1 and h>0):
        rt=rt-ele_copy[h]
        h=h-1
    #print(h)
    su=rt%ele_copy[h]
    #print(su)
    
    if(len(ele)!=0):
        rem=[0]*n
        #print(ele)
        while(len(ele)>1):
            ma=max(ele)
            inx=ele_copy.index(ma)
            inx1=ele.index(ma)
            rem_n=p%ma
            rem[inx]=math.floor(p/ma)
            p=p%ma
            #print("###",ele)
            #print("***",inx1)
            ele.remove(ma)
            #print(ele)
        inx=ele_copy.index(ele[0])
        rem[inx]=math.ceil(p/ele[0])
        print("YES",end=" ")
        for i in range(len(rem)-1):
            print("{}".format(rem[i]),end=" ")
        print("{}".format(rem[len(rem)-1]))
    elif(len(ele)==0 and su!=0):
        reg=[0]*len(ele_copy)
        reg[0]=int(p/ele_copy[0])
        reg[1]=1
        print("YES",end=" ")
        for i in range(len(reg)-1):
            print("{}".format(reg[i]),end=" ")
        print("{}".format(reg[len(reg)-1]))
    else:
        print("NO")