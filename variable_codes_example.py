# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 09:19:16 2020

@author: alan.martinez.blanco
@title: variables example code
"""

#Ask the user for the radius of a circle and then print the area
# radius = float(input("Please enter the circle radius: "))
# pi = 3.14159
# area = pi * radius**2
# print("You entered",radius, "the area of the circle is ",area)

#Conver Fahrenheit to Celcius
# far = float(input("Please enter the Fahrenheit temperature: "))
# cel = (far - 32) * 5/9
# print(far, "in celsius is ", cel)

# #Obtain the sum of two integers
# number1 = int(input("Please enter the first number: "))
# number2 = int(input("Please enter the second number: "))
# sumres = number1 + number2
# print("The sum of ", number1, " and ", number2, " is ", sumres)

# #Obtain the product of two integers
# number1 = int(input("Please enter the first number: "))
# number2 = int(input("Please enter the second number: "))
# sumres = number1 * number2
# print("The product of ", number1, " and ", number2, " is ", sumres)

#Bob, Ann, Jane and Ashwin want to order pizza - they know they will eat 4 slices
# of pizza. The local pizza shop sells pizzas of only 6 slices
#what is the minimun number of pizzas needed- use floor division

total_slices = 16
number_of_pizzas = (total_slices + 5)//6
slices_left= number_of_pizzas*6 - total_slices
print("Number of pizzas needed ", str(number_of_pizzas), "there will be ", str(slices_left), "slices left")