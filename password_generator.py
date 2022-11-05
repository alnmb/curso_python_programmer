"""
Title: Password generator
Creator: Alan Martinez


"""
import random, string, pyperclip

option = "Y"

while option == "Y":
    pass_length = int(input("Cual sera el largo de la contrasena: "))
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = []
    for x in range(pass_length):
        password.append(random.choice(password_characters))

    pwd = ("".join(password))
    print("La contraseña es: ", pwd)
    pyperclip.copy(pwd)
    pyperclip.paste()
    
    option = input("Necesitas otra contraseña?(Y/N): -> ")
    option = option.upper()
    
    if option == "N":
        print("Gracias vuelve a usarme despues :) ")
        break



