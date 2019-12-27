# Password Generator
import random
import string

print("Hello. This program will generate a random and secure password using letters, numbers, capitalization, and special characters that is up to 39 characters long.")
print("If the password generated is too long, simply use just a portion as your passcode. If it is too short, simply run the program agian and generate a second password to combine with the first.")

length = 0

animals = ['tiger', 'moose', 'mouse', 'fox', 'zebra', 'cow', 'bison', 'armadillo', 'wolf', 'lion', 'monkey']
password = random.choice(animals)
specialChar = ['!', '@', '#', '$', '%','^','&','*', '(', ')','-','_', '+','=','|','|','?','>','<','/','.',',']
for i in range(0, 10):
    password = password + str(random.randint(0,99))
    password = password + random.choice(string.ascii_letters)
    password = password + random.choice(specialChar)
print(password)
