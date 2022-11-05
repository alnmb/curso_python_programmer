# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:47:15 2021

@author: alan.martinez.blanco
@title: function_questions

"""

"""Question 1
Create a function that will calculate the sum of two numbers 
call it sum_two"""

# def sum_two(a,b):
#     return a+b

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# res = sum_two(a,b)

# print(str(res))

"""
Question 2
Write a function that performs multiplicationof two arguments. by default the function should multiply the first argument by 2.
call it multiply"""

# def multiply(a,b=2):
#     return a*b

# a = 6
# b = 4
# c = multiply(a,b)
# print(c)

"""
Question 3
Write a function to calculate a to the power of b
If b is not given 
its default value should be 2 call it power
"""

# def power(a,b=2):
#     return a**b

# c = power(5,30)

# print(f'El valor de potencia es:{c} ')

"""
Question 4
Create a new file called capitals.txt, store the names of five capital cities in the file 
on the same line

"""

# f = open("C:/Users/alan.martinez.blanco/Desktop/python course/capitals.txt", 'w')

# f.write("Paris, ")
# f.write("Washington, ")
# f.write("CDMX, ")
# f.write("Tokyo, ")
# f.write("London.")

# f.close()

"""
Question 5
Write some code that requests the user to input another capital city
add that city to the list of cities in capitals
then print the file to the screen
"""
# f = open("C:/Users/alan.martinez.blanco/Desktop/python course/capitals.txt", "a")

# user_input = input("Enter a capital here: ")

# f.write(" "+user_input+", ")

# f.close()

"""
Question 6
Write a function that will copy the contents of one file to a new file
"""

# def copy_file(file):
#     f1 = open(file, "r")
#     f2 = open("C:/Users/alan.martinez.blanco/Desktop/python course/copy.txt","w")
    
#     f2.write(f1.read())
#     f1.close()
#     f1.close()
#     print("File copied")

# v = copy_file("C:/Users/alan.martinez.blanco/Desktop/python course/capitals.txt")



