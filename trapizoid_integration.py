# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 00:28:51 2021

@author: User
"""


import numpy as np
from tabulate import tabulate
def fx(x):
    return ((2000*np.log(140000/(140000-2100*x)))-9.8*x)

def integratoin(n,a,b):
    h=(b-a)/n
    s=(fx(a)+fx(b))/2
    for i in range(1,n,1):
        s+=fx(a+i*h)
    return h*s
    
    
    
def main():
    value=integratoin(8, 8, 30)
    print(value)
    table=[]
    old_v=0
    for i in range(1,6,1):
        v=integratoin(i, 8,30)
        if(i>1):
            err=abs((value-v)/value*100)
            table.append([i,v,err])
        else:
             table.append([i,v,"--"])
        old_v=v
    print(tabulate(table,headers=["value","error"]))
    
main()    
    
    
    
    
    