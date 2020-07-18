# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:07:33 2020

@author: MADCAT
"""
pri_list=[]

n=int(input("pls enter an integer:"))

for i in range(2,n+1):
    if i == 2 :
        pri_list.append(i)
    else:
        for x in range(2,i):
           
            if i % x == 0 :
                break
            elif x == i-1 :
                pri_list.append(i)
            else:
                continue
print(pri_list)
    

            