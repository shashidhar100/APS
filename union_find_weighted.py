# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:32:29 2020

@author: shashidhar
"""
n=6
size=[1]*n
root=[i for i in range(n)]
def union(u,v):
    if size[root[u]]<size[root[v]]:
        
        root[u]=root[v]
        size[root[v]]+=size[root[u]]
    else:
        root[v]=root[u]
        size[root[u]]+=size[root[v]]

union(0,1)
union(1,2)
union(3,2)
