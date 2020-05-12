# Uses python3

def binary_search(a, x,left,right):
    if left>right:
        return -1
    mid=(left+((right-left)//2))
    if x==a[mid]:
        return mid
    elif x<a[mid]:
        return binary_search(a,x,left,mid-1)
    else:
        return binary_search(a,x,mid+1,right)
        
    
    
    
    

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    lis=list(map(int,input().split(" ")))
    que=list(map(int,input().split(" ")))
    del lis[0]
    del que[0]
    for i in range(len(que)):
       k=binary_search(lis,que[i],0,len(lis)-1)
       print(k,end=" ")

# 5 1 5 8 12 13
# 5 8 1 23 1 11