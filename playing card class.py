# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:23:34 2021

@author: aln_m
@title: playing card class
"""

class card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def displayValue(self):
        return self.value
    
    def displaySuit(self):
        return self.suit
    
    def __str__(self):
        my_card = str(self.value) + ' of '+str(self.suit)
        return my_card
    

