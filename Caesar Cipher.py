# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:48:34 2021

@author: aln_m
@title: caesar cipher
"""

"""
formula:
    
c = (x+n)%26
c = encrypted
x = original text
n = cipher number
26 = letters in eng alphabet
"""
def shift(i):
    return i%26
    
def encrypt(text,n):
    text = text.lower()
    result = ""
    alphabet = "abcdefghikjlmnopqrstuvwxyz"
    
    for char in text:
        if char not in alphabet:
            result = result + char
        else:
            alpha = alphabet.find(char)
            result = result+alphabet[shift(alpha+n)]
        
    return result

text = "Once when I was six years old I saw a magnificent picture in a book, called True Stories from Nature, about the primeval forest. It was a picture of a boa constrictor in the act of swallowing an animal. Here is a copy of the drawing."       
crypted = encrypt(text,3)
print("Encripted")
print(crypted)
decripted = encrypt(crypted,-3)
print("Decripted")
print(decripted)            
            
            