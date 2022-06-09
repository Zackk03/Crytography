from operator import le
from optparse import BadOptionError
from tqdm import tqdm
import os
import time
import sqlite3 as sql
from prettytable import from_db_cursor

#----------banners
banner1 = """
[*] Now, type the text to encrypt [*]


"""
banner2 = """
[*] The offset should be 1 - 8 [*]


"""

banner3 = """
███████╗ ██████╗ ██████╗ ██████╗ ██╗   ██╗      
██╔════╝██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝      
███████╗██║   ██║██████╔╝██████╔╝ ╚████╔╝       
╚════██║██║   ██║██╔══██╗██╔══██╗  ╚██╔╝        
███████║╚██████╔╝██║  ██║██║  ██║   ██║██╗██╗██╗
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝╚═╝╚═╝╚═╝
                                                
"""

#--------Creating the data base
def createdb():
    conn = sql.connect("keys.db")
    conn.commit()
    conn.close()

#-----------------------------OJO-----------------------------------#
#tables
def createtable():
    conn = sql.connect("keys.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE cipher_keys(
        origin varchar(100) PRIMARY KEY,
        cipher varchar(500),
        original varchar(500))
        """)
    conn.commit()
    conn.close()

#--------main function to encrypt texts or passwords
def encrypt():
    #r u sure?
    print()
    print()
    ausure = input("¿Are you sure do you want Encrypt a key? [yes/no]: ")
    if ausure == "no" or ausure == "n":
        pass
    elif ausure == "yes" or ausure == "y":

        #Database Initialization-----------------------------------OJO
        conn = sql.connect("keys.db")
        cursor = conn.cursor()

        #introducing the text to encypt
        os.system("cls")
        print(banner1)
        
        #--------Process control using a flag
        flag = True
        while flag:
            os.system("cls")
            print(banner1)
            text = input("Type the text you want encrypt: ")
            if text == "":
                print()
                print()
                print("Please, Do not let the field empty: ")
                input()
            else:
                flag = False
        
        #this condition, we used to determinate if the text is minus or mayus
        if text==text.upper():
            abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZABC"
        else:
            abc = "abcdefghijklmnñopqrstuvwxyzabc"

        
        #offset value
        os.system("cls")
        print(banner2)
        k = int(input("Type the offset value: "))

        #Origin of the text, if it is a facebook key, IG key or just a note
        print()
        origin = input("Origin of the text (IG,FB,WS,NOTE...): ")

        #where we storage the key...
        cipher = ""

        #progress bar
        os.system("cls")
        for i in tqdm(range(5)):
            time.sleep(0.2)

        #algorithm used to cipher the text
        try:
            for c in text:
                if c in abc:
                    cipher += abc[(abc.index(c)+k%(len(abc)))]
        except:
                    cipher+=c

        #showing the original text, encrypted text and the origin...
        os.system("cls")
        print("[*]   " + origin.capitalize() + " ----------:>> " + (text) + " ---:>> " + str(cipher.replace(" ", "")) + "   [*]")
        print()
        try:
            save = input("¿Would you like save the key? Y/N: ")
            if save == "y" or save == "yes":
                os.system("cls")
                print("Saving...")
                time.sleep(2)
                cursor.execute(f"INSERT INTO cipher_keys VALUES ('{(origin.capitalize())}','{cipher}','{text}')")
                conn.commit()
                conn.close()
            else:
                os.system("cls")
                print("Canceling...")
                time.sleep(2)
                pass
        except:
            os.system("cls")
            print("Sorry, this origin already exist, please try typing a new one...")
            time.sleep(4)

        # except:
        #     print("Type a valid option please (yes or no)...")
        #     time.sleep(3)

#--------Showing the saved keys
def showkey():
    os.system("cls")
    conn = sql.connect("keys.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM cipher_keys")
    x = from_db_cursor(cursor)
    print(x)
    input("Type Enter to continue...")

def showkey1():
    os.system("cls")
    conn = sql.connect("keys.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM cipher_keys")
    x = from_db_cursor(cursor)
    print(x)

#--------deleting rows of the table
def deletekey():
    try:
        os.system("cls")
        conn = sql.connect("keys.db")
        instruction = "SELECT * FROM cipher_keys"
        cursor = conn.cursor()
        cursor.execute(instruction)
        keys = cursor.fetchall()
        showkey1()
        print()
        print()

        question = input("What key do you want delete? Type the origin of it: ")

        for i in range(len(keys)):
            origin = keys[i][0]
        
        if origin != question.capitalize():
            os.system("cls")
            print(banner3)
            print("we couldn't find the origin, please try again...")
            print(origin)
            time.sleep(4)

        else:
        
            instruction1 = f"DELETE FROM cipher_keys where origin='{question.capitalize()}'" 
            
            os.system("cls")
            print("Deleting...")
            time.sleep(2)
            
            cursor.execute(instruction1)
            conn.commit()
            conn.close()
    except:
        os.system("cls")
        print(banner3)
        print("we couldn't find the origin, please try again...")
        time.sleep(4)
        

#--------executing functions...
if __name__ == "__main__":
    #cifrar()
    createdb()
    createtable()
    #cleardb("")
    #deletekey()