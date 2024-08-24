print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

name = name1 + name2
name = name.lower()

true_count = 0
true_count += name.count("t")
true_count += name.count("r")
true_count += name.count("u")
true_count += name.count("e")

love_count = 0
love_count += name.count("l")
love_count += name.count("o")
love_count += name.count("v")
love_count += name.count("e")

print(f"{true_count}{love_count}")