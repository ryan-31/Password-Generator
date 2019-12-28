# Password Generator
import random
import string
import tkinter
mainWin = tkinter.Tk()

mainWin.title("Password Generator")
txtLbl1 = tkinter.Label(mainWin, text = "Hello. This program will generate a random and secure up to 35 character password using letters, numbers, capitalization, and special characters.", font = ("Times New Roman", 14))
txtLbl2 = tkinter.Label(mainWin, text = "If the password generated is too long, simply use just a portion as your passcode. If it is too short, simply run the program agian and generate a second password to combine with the first.", font = ("Times New Roman", 14))
txtLbl3 = tkinter.Label(mainWin, text = "This password generator does not save/store passwords created.", font = ("Times New Roman", 14))
txtLbl1.pack()
txtLbl2.pack()
txtLbl3.pack()


from tkinter import Text

pswrd = Text(mainWin,height = 1)

def generate():
    pswrd = Text(mainWin,height = 1)
    # clearing previous password
    password = " "
    specialChar = ['!', '@', '#', '$', '%','^','&','*', '(', ')','-','_', '+','=','|','|','?','>','<','/','.',',']
    animals = ['DIng0', 'Mo0se', 'mOusE', 'sHeEP', 'zEbRa', 'sKuNk', 'BiSoN', 'wHAle', 'KoALa', 'LemUR', 'hYEnA', 'CaMEl','cHImP', 'RhinO' ]
    #initialize password with a random animal
    password = random.choice(animals)
    for i in range(0, 9):
        password = password + str(random.randint(0,9))
        password = password + random.choice(string.ascii_letters)
        password = password + random.choice(specialChar)
    pswrd.insert(1.0, password)
    pswrd.pack()
    pswrd.configure(state = "disabled")
    pswrd.configure(bg=mainWin.cget('bg'), relief="flat")
        
from tkinter import Button
b = Button(mainWin, text ="Generate", command=generate)
b.pack()



mainWin.mainloop()
