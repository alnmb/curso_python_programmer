# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:41:21 2021

@author: aln_m
@title: two sum problem
"""



def twoSum(Lista, Target):
    for a in range(len(Lista)):
        for b in range(a+1,len(Lista)):
            suma = Lista[a] + Lista[b]
            if  suma == Target:
                print(Lista[a])
                print(Lista[b])
                return suma


Lista = [2,5,3,7,8,3,2,8,4]
Target = 13
res = twoSum(Lista,Target)
print(res)
