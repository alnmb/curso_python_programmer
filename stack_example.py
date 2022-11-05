# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 22:00:59 2021

@author: aln_m
@title: stack class example
"""

class stack():
    def __init__(self):
        self.list_stack = []
    def is_empty(self):
        if not self.list_stack:
            return True
        else:
            return False
    def push(self,item):
        self.list_stack.append(item)
    def pop(self):
        return self.list_stack.pop()
    def peek(self):
        if self.list_stack == []:
            return None
        else:
            return self.list_stack[-1]
    """repr in class: is similar to str to output content from the class
    str is mainly for end users versus repr is used mostly for debugging"""
    def __repr__(self): 
        return repr(self.list_stack)
