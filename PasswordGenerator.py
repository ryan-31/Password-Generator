# --------------------------------------------------------------------------------------------------
# Created by Ryan S (GitHub: ryan-31)
# Updated 9/26/21
# Fully utilized random(), added password customization, added entry widget and radio buttons
# Version 3.0
# ---------------------------------------------------------------------------------------------------

import random
import string
import tkinter
from tkinter import *


def create_pass():
    password = ""

    length = int(passLength.get())
    symbols = sym.get()

    if not symbols:
        for i in range(length):
            password = password + random.choice(string.ascii_letters + string.digits)
    else:
        for i in range(length):
            password = password + random.choice(string.ascii_letters + string.digits + string.punctuation)

    generated_pass.config(text=password)
    generated_pass.config(font=('helvetica', 16))
    generated_pass.pack()


root = Tk()
root.title = "Password Generator"
root.geometry('800x600')

titleLabel = Label(root, text="Password Generator")
titleLabel.config(font=('helvetica', 20))
titleLabel.pack()

subTitle = Label(root, text='A secure password is very important\nin keeping your accounts safe from hackers and cyber'
                            'criminals!\n\n')
subTitle.config(font=('consolas', 12))
subTitle.pack()

lengthLabel = Label(root, text='Enter your desired password length:')
lengthLabel.config(font=('helvetica', 14))
passLength = StringVar()
lengthEntry = tkinter.Entry(root, textvariable=passLength)
lengthLabel.pack()
lengthEntry.pack()

symbolsLabel = Label(root, text='Would you like to include symbols?')
symbolsLabel.config(font=('helvetica', 14))
sym = tkinter.BooleanVar()
symbolsRadio = Radiobutton(root, text='Yes', variable=sym, value=True)
symbolsRadio.config(font=('helvetica', 14))

symbolsRadio2 = Radiobutton(root, text='No', variable=sym, value=False)
symbolsRadio2.config(font=('helvetica', 14))

symbolsLabel.pack()
symbolsRadio.pack()
symbolsRadio2.pack()

# Generate Password Button
generate = Button(root, text='Generate Password', command=create_pass)
generate.pack()

generated_pass = Label(root, text='')


root.mainloop()
