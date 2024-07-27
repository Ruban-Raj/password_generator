#Password Generator Project
import random
import string_utils
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like out of the above mentioned letter?\n"))
nr_numbers = int(input(f"How many numbers would you like out of the above mentioned letter?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

random_let = ""
random_sym = ""
random_num = ""
for n in range(0, nr_symbols):
    random_sym = random_sym + random.choice(symbols)

for n in range(0, nr_numbers):
    random_num = random_num + random.choice(numbers)
    
for n in range(0, nr_letters - nr_numbers - nr_symbols):
    random_let = random_let + random.choice(letters)
    
pwd = random_num + random_sym + random_let
pwd_random = string_utils.shuffle(pwd)
print(f"Your password is: {pwd_random}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P