# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:05:13 2021

@author: aln_m
@title: classes, objects and inheritance questions
"""

"""
Question 1
Create a class to represent a bank account. 
It will need to have a balance a method of withdrawing money, 
depositing money and displaying the balance to the screen. 
Create an instance of the bank account 
and check that the methods works as expected

"""

# class BankAccount(object):
    
#     def __init__(self, balance=0.0):
#         self.balance = balance
    
#     def withdraw(self):
#         amount = float(input('How much money do you want to withdraw? -> '))
#         if amount > self.balance:
#             print('You dont have this amount of money in your account')
#         else:
#             self.balance = self.balance - amount
#             print(f'Your new balance is :${self.balance}')
            
#     def deposit(self):
#         amount = float(input('How much money do you want to deposit? -> '))
#         self.balance = self.balance + amount
        
#     def displayBalance(self):
#         print(f'Your balance is:${self.balance}')

# cuentaAlan = BankAccount(3000)

"""
Question 2
Create a circle class that will take the value 
of a radius and return the area of the circle
"""
import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    
    def CalculateArea(self):
        radius = pow(self.radius,2)
        area = math.pi * radius
        print(f'The area of the circle is: {area} with a radius of: {radius}')
    

        