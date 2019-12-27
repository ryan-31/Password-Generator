# Password Generator
import random
import string
import tkinter

mainWin = tkinter.Tk()

mainWin.title("Password Generator")
txtLbl1 = tkinter.Label(mainWin, text = "Hello. This program will generate a random and secure password using letters, numbers, capitalization, and special characters that is 35 characters long.", font = ("Times New Roman", 14))
txtLbl2 = tkinter.Label(mainWin, text = "If the password generated is too long, simply use just a portion as your passcode. If it is too short, simply run the program agian and generate a second password to combine with the first.", font = ("Times New Roman", 14))
txtLbl3 = tkinter.Label(mainWin, text = "This password generator does not save/store passwords created.", font = ("Times New Roman", 14))
txtLbl1.grid(column = 0, row = 0)
txtLbl2.grid(column = 0, row = 1)
txtLbl3.grid(column = 0, row = 2)

txtLbl4 = tkinter.Label(mainWin, text = " ", font = ("Times New Roman", 13))

def generate():
    # clearing previous text
    password = " "
    specialChar = ['!', '@', '#', '$', '%','^','&','*', '(', ')','-','_', '+','=','|','|','?','>','<','/','.',',']
    animals = ['DIng0', 'Mo0se', 'mOusE', 'sHeEP', 'zEbRa', 'sKuNk', 'BiSoN', 'wHAle', 'KoALa', 'LemUR', 'hYEnA', 'CaMEl','cHImP', 'RhinO' ]
    #initialize password with a random animal
    password = random.choice(animals)
    for i in range(0, 10):
        password = password + str(random.randint(0,99))
        password = password + random.choice(string.ascii_letters)
        password = password + random.choice(specialChar)
        txtLbl4 = tkinter.Label(mainWin, text = password, font = ("Times New Roman", 12))
        txtLbl4.grid(column = 0, row = 4)
        

from tkinter import Button
b = Button(mainWin, text ="Generate", command=generate)
b.grid(column = 0, row = 3)



mainWin.mainloop()
