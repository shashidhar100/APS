# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 17:51:02 2020

@author: shashidhar
"""
s1='musicalff'
s2='classicalfhhhhf'
le_s1=len(s1)+1
le_s2=len(s2)+1
lcc=[[0] * le_s2 for i in range(le_s1)]  
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            lcc[i+1][j+1]=lcc[i][j]+1
        else:
            lcc[i+1][j+1]=max([lcc[i][j+1],lcc[i+1][j]])
        
print(lcc[len(s1)][len(s2)])        

