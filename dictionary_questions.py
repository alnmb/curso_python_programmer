# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:59:29 2021
"title: Dictionaries questions"
@author: alan.martinez.blanco
"""

"""
Question 1
Can you remember hoqw to check if a key exits in a dictionary?
Using the capitals dictionary write some code to ask the user to input a country, 
then check to see if that country is in the dictionary and if it is print the capital. If not tell the user its not there

"""
# capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London','India':'New Delhi',
#             'United States':'Washington','Italy':'Rome','Mexico':'CDMX'}

# userCountry = input("Enter a country: ")
# if userCountry in capitals.keys():
#     print("The capital of ",userCountry ," is ", capitals[userCountry])
# else:
#     print("No data available")
    
"""
Question 2
Write python code that will create a dictionary containing key, value pairs 
that represent the first 12 values of the fibonacci sequence
ie {1:0,2:1,3:1,4:2,5:3,6:5,7:8}
"""
# n = 12
# a = 0
# b = 1
# d = dict()

# for i in range(1, n+1):
#     d[i] = a
#     a,b = b, a+b

# print(d)

"""
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87,13.23,11.42,13.10], [23,54,25.76,21.87,22,33],
[98,99,102,34,97.21,100,0.65], [203,63,207,54,202,43,205,24]

"""

# companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
# key_names = ['Open','High','Low','Close']

# prices = [[12.87,13.23,11.42,13.10], [23,54,25.76,21.87,22,33],
# [98,99,102,34,97.21,100,0.65], [203,63,207,54,202,43,205,24]]|

# d_1= {}

# for i in range(len(key_names)):
#     d_1[companies[i]] = dict(zip(key_names,prices[i]))
    
# print(d_1)

"""
Question 4
Go to the python module web page and find a module that you like.
play with it read the documentation and try to implement
"""

# import keyword

# user_input = input("Enter a word -> ")
# user_input = user_input.lower()

# keyword = keyword.iskeyword(user_input)
# keyword = str(keyword)
# print(keyword)
# if keyword == "True":
#     print("It's a keyword!!")
# else:
#     print("It is not a keyword")

"""
Question 5
Create a dictionary containing as keys the letters from A-Z, 
the values should be random numbers created from the random module, can you draw a bar graph of the results?
"""
import random, matplotlib.pyplot as plt
keys = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'

d = dict()

for i in keys:
    d[i] = random.randint(1, 100)

print(d)

x,y = zip(*d.items())
plt.bar(x,y)

