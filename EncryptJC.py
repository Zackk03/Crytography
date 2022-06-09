from ast import Delete
import os
from winreg import DeleteKey
from funciones import *
import time

#Banners
banner = """
[*] Program to encrypt passwords. Let´s Encrypt!!... [*]

(1) Encrypt
(2) Show Keys
(3) Delete Keys
(4) Exit

Auth: Erick Garcia Mendez 


"""

#--------main program
flag = True
while flag:
    #try all this...
    #try:
    os.system("cls")
    print(banner)

    #selection question
    option = int(input("choose one of these options: "))

    #decisions tree
    if option == 1:
        encrypt()
    elif option == 2:
        showkey()
    elif option == 3:
        deletekey()
    elif option == 4:
        question = input("¿Are you sure, do you want exit? y/n: ")
        if question == "y":
            print()
            print("exiting...")
            time.sleep(2)
            flag = False
        else:
            os.system("cls")
            pass
    # else:
    #     print()
    #     print()
    #     print("Type a valid option please...")
    #     time.sleep(3)
    #     pass
    #if the program failed, execute this...
    # except:
    #     print()
    #     print()
    #     print("Type a valid option please...")
    #     time.sleep(3)
    #     pass

