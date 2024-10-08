import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for n in range(0, nr_letters):
#   user_pw += random.choice(letters)

# for n in range(0, nr_symbols):
#   user_pw += random.choice(symbols)

# for n in range(0, nr_numbers):
#   user_pw += random.choice(numbers)
  
# print(f"Here is your password: {user_pw}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

user_pw = []

for n in range(0, nr_letters):
  user_pw.append(random.choice(letters))

for n in range(0, nr_symbols):
  user_pw.append(random.choice(symbols))

for n in range(0, nr_numbers):
  user_pw.append(random.choice(numbers))
  
random.shuffle(user_pw)

password = ""

for pw in user_pw:
  password += pw

print(f"Here is your password: {password}")

