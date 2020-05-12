# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:18:42 2020

@author: shashidhar
"""

def bc(n,k):
    if(n==k or k==0):
        return(1)
    else:
        return bc(n-1,k-1)+bc(n-1,k)
print(bc(5,2))