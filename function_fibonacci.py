# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:58:55 2021

@author: alan.martinez.blanco
@title: fibonacci code function

"""
def fibonacci_code(n):
    a = 0
    b = 1   

    fib = []

    for i in range(n):
        fib.append(a)
        a,b = b, a+b
    return fib

n = int(input("Enter a number: "))

print("The fibonacci "+str(n)+" numbers are: ")

fib = fibonacci_code(n)
print(fib)
