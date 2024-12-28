letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

ran_letter = ''
ran_symbols = ''
ran_numbers = ''


for n in range(0, nr_letters):
    ran_letter = ran_letter + random.choice(letters)

for n in range(0, nr_symbols):
    ran_symbols = ran_symbols + random.choice(symbols)

for n in range(0, nr_numbers):
    ran_numbers = ran_numbers + random.choice(numbers)

print(ran_letter)
print(ran_numbers)
print(ran_symbols)

pass_selected = ran_symbols + ran_numbers + ran_letter

pwd_list = list(pass_selected)
print(pwd_list)
random.shuffle(pwd_list)

#list to string
hard_pwd = ''.join(pwd_list)

print(f"your easy level pwd is {pass_selected}\n and your hard pwd is {hard_pwd}")


