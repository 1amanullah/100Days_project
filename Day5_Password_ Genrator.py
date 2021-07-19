import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password genrator!!")
letters_let = int(input("How many letters would you like in your password? \n"))
symbols_sym = int(input("How many symbols would you like in your password? \n"))
numbers_num = int(input("How many numbers would you like in your password? \n"))

#EASY PASSWORD

# password = ""
# for char in range(1,letters_let+1):

# 	password += random.choice(letters)

# for char in range(1,symbols_sym+1):

# 	password += random.choice(numbers)

# for char in range(1,numbers_num+1):

# 	password += random.choice(symbols)

# print(password)

#-----------------------------------------------------------------

#HARD PASSWORD

list_password = []
for char in range(1,letters_let+1):

	list_password.append(random.choice(letters))

for char in range(1,symbols_sym+1):

	list_password.append(random.choice(numbers))

for char in range(1,numbers_num+1):

	list_password.append(random.choice(symbols))


random.shuffle(list_password)


password = ""
for char in list_password:

	password += char

print(password)
