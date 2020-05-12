# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 17:17:28 2020

@author: shashidhar
"""
N=int(input())
results=[]
for i in range(100):
    results.append(0)
for i in range(2,N+1):
    
    for j in range(1,(i//2)+1):
        lis=[]
        lis.append(results[i])
        lis.append(j*(i-j))
        lis.append(j*results[(i-j)])
        m=max(lis)
        results[i]=m
print(results[N])
        
        


