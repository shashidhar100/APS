# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    c_r=0
    n_r=0
    while(c_r<=len(stops)-2):
        l_r=c_r
        while(c_r<=n and (stops[c_r+1]-stops[l_r]<=tank)):
            c_r=c_r+1
        if c_r==l_r:
            return -1
        if c_r<=n:
            n_r+=1
    
    return n_r

if __name__ == '__main__':
    d=int(input())
    m=int(input())
    n=int(input())
    lis=list(map(int,input().split(" ")))
    lis[0:0]=[0]
    lis.append(d)
    print(compute_min_refills(d, m, lis))
# 950
# 400
# 4
# 200 375 550 750