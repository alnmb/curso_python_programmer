# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 09:48:34 2020

@author: alan.martinez.blanco
@title: conditional questions
"""

"""Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
the code will take the integer value and print out the string value. 
So for example if the user inputs 2 the code will print two. 
Reject any input that is not a number in that range
"""

# number = int(input("Input a number between 1 and 5: "))

# if number == 1:
#     print("The number is one")
# elif number == 2:
#     print("The number is two")
# elif number == 3:
#     print("The number is three")
# elif number == 4:
#     print("The number is four")
# elif number == 5:
#     print("The number is five")
# else:
#     print("Please introduce a number between 1 and 5, thanks")

"""
Question 2
Repeat the previous task but this time the user will input a string and the code will ouput the integer value. 
Convert the string to lowercase first
"""

# number = input("Input a string number from one to five: ")
# number = number.lower()

# if number == "one":
#     print("The number is 1")
# elif number == "two":
#     print("The number is 2")
# elif number == "three":
#     print("The number is 3")
# elif number == "four":
#     print("The number is 4")
# elif number == "five":
#     print("The number is 5")
# else:
#     print("Please introduce a number between 1 and 5, thanks")

"""
Question 3
Create a variable containing an integer between 1 and 10 inclusive. 
Ask the user to guess the number. If they guess too high or too low, tell them they have not won. 
Tell them they win if they guess the correct number"""

# number = 4
# guess = int(input("Give a number between 1 and 10: "))

# if guess == number:
#     print("Yay you have won!!")
# elif guess > number and guess <= 10:
#     print("Too bad you lost ",str(guess)," is not the number I was thinking it was too high")
# elif guess < number and guess >= 1:
#     print("Too bad you lost ",str(guess)," is not the number I was thinking it was too low")
# else:
#     print("Out of range")


"""Question 4
Ask the user to input their name. Check the length of the name. 
If it is greater than 5 characters long, write a message telling them how many characters 
otherwise write a message saying the length of their name is a secret
"""
# name = input("Please tell me your name: ")
# len_name = len(name)

# if len_name >= 5:
#     print("Your name is ", name, " and has ", len_name, " characters")
# else:
#     print("The length of your name is a secret")

"""
question 5
ask the user for two integers between 1 and 20. If they are both greater than 15 return their product
If only one is greater than 15 return their sum, if neither are greater than 15 return 0"""

# num1 = int(input("please give a number: "))
# num2 = int(input("please give another number: "))
# res = 0
# if (num1 > 1 and num1 <= 20) and (num2 > 1 and num2 <= 20):
#     if num1 >= 15 and num2 >= 15:
#         res = num1 * num2
#         print(int(res))
#     elif num1 >= 15 or num2 >= 15:
#         res = num1 + num2
#         print(int(res))
#     else:
#         print(0)
# else:
#     print("both numbers should be shorter than 20")
 
"""Question6 
ask the user for two integers, then swap the contents of the variables. so if var_1 = 1
and var_2 = 2 initially, once the code has run var_1 should equal 2 and var_2 should equal 1
"""
num1 = int(input("please give a number: "))
num2 = int(input("please give another number: "))
print("Before swap num1 is: ", num1, "and num2 is: ", num2)
num1, num2 = num2, num1
print("After swap num1 is: ", num1, "and num2 is: ", num2)