# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:42:29 2021

@author: alan.martinez.blanco
@title: reading files


"""

"""recomended method to open files"""
book = "C:/Users/alan.martinez.blanco/Desktop/python course/theAdventuresOfSherlockHolmes.txt"
# with open(book,'r') as f:
#     for line in f.readlines():
#         print(line, end="")
        
"""
non recommended method
"""

f = open(book,'r')
for line in f.readlines():
    print(line, end="")

f.close()

