# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:10:45 2020

@author: shashidhar
"""
def catlon(n):
    x=2*m.factorial(n)
    y=m.factorial(n+1)
    z=m.factorial(n)
    cat=x/(y*z)
import numpy as np
import math as m
def inc_y(x,y,n):
    while(y<=n):
        y=y+1
        inc_y(x,y,n)
        inc_x(x,y,n)
        print("({},{})".format(x,y))
    print("\n")
def inc_x(x,y,n):
    while(x<=n):
        print("({},{})".format(x,y))
        x=x+1


        
    
    
n=int(input("enter the number"))
inc_y(0,0,n)



