# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 23:26:13 2021

@author: aln_m
"""

"""
stacks challenge
balance brackets
crete a function take string input made of brackets 
has to check the right order of open and closed brackets
{[()]} = returns true
({[}]) = returns false


"""
def balanced_brackets(s):
    stack = []
    brackets = {"(":")", "[":"]", "{":"}"}
    
    for char in s:
        if char in brackets.keys():
            stack.append(char)
        else:
            if len(stack) == 0 or brackets[stack.pop()] != char:
                return False
    return len(stack) == 0


string = "[[({})]]"
print(balanced_brackets(string))            