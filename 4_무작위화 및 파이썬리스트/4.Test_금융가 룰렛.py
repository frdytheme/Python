import random

names_string = input("what is their names? a, b, ..., z: ")
names = names_string.split(", ")
num_items = len(names)
random_num = random.randint(0, num_items - 1)

print(f"{names[random_num]} is going to buy the meal today")

