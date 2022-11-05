# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:23:29 2021

@author: alan.martinez.blanco
@title: loop_questions
"""

"""Question 1
Ask the user for two numbers between 1 and 100. then count from the
lower number to the higher number. print the results to the screen"""

# num1 = int(input("Please enter a number between 1 and 100: "))
# num2 = int(input("Please enter a second number between 1 and 100: "))

# while num1 <= 0 or num2 <= 0 or num1 > 100 or num2 > 100 or num1 == num2:
#     print("Numbers must be different values between 1 and 100. Try again")
#     num1 = int(input("Please enter a number between 1 and 100: "))
#     num2 = int(input("Please enter a second number between 1 and 100: "))

# if num1 < num2:
#     for i in range(num1, num2+1):
#         print(i, end=' ')
# else:
#     for i in range(num2, num1+1):
#         print(i, end=' ')
    
"""
question 2
ask the user to input a string and then print it out to the screen in reverse order (use a for loop)
"""

# text = input("Please enter a text so I can reverse it: ")
# reverse = "" 
# for c in text:
#     reverse = c + reverse
# print(reverse)
# print(text[::-1])

"""
question 3
ask the user for a number between 1 and 12 and then display a times table 
for that number"""

num = int(input("Please enter a number between 1 and 12: "))

while num <= 0 or num > 12:
    print("Please enter a valid number between 1 and 12")
    num = int(input("Please enter a number between 1 and 12: "))

print("***********")
print()
for i in range(1, 13):
    print(i, " x ", num, " = ", i*num)

print("***********")

"""
question 4
can you amend the solution to question 3 so that it just prints out a
times table between 1 and 12? no need to ask for user input"""

# for i in range(1, 13):
#     print("=================")
#     print()
#     print("This is the ", i, "times table")
#     print()
#     for j in range(1, 13):
#         print(i, " x ", j, " = ", i*j)
#     print("=================")

"""
question 5
ask the user to input a sequence of numbers, then calculate the mean 
and print the result"""

# user_input = int(input("Please enter a number: "))
# numbers = []
# while user_input != "exit":
#     numbers.append(int(user_input))
#     user_input = input("Please enter a number: ")
# total = 0

# for i in numbers:
#     total += i

# mean = total / len(numbers)
# print(mean)

"""
question 6
write code that will calculate 15 factorial (factorial is product of 
positive ints up to a given number e.g. 5 factorial is 5x4x3x2x1)"""

# fact = 1
# for i in range(1, 16):
#     fact = fact * i

# print(fact)

"""
question 6.5
modify question 6 now with user input"""

# user_input = int(input("Please enter a number: "))
# fact = 1
# for i in range(1, user_input+1):
#     fact = fact * i
    
# print(fact)

"""
question 7
write code to calculate fibonacci numbers.
create list containing first 20 fibonacci numbers (fib numbers made by sum of 
preceeding two, series starts 0 1 1 2 3 5 8 13 19)
"""

# n = 20
# a = 0
# b = 1

# fib = []

# for i in range(n):
#     fib.append(a)
#     a,b = b, a+b
    
# print(fib)

""" question 10
write some code that will determine all odd and even numbers
between 1 and 100. put the odds in a list named odd and the evens
in a list named even"""

# odd = []
# even = []

# for i in range(1, 101):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
        
# print("Evens: ")
# print(even)
# print()
# print("Odds: ")
# print(odd)

