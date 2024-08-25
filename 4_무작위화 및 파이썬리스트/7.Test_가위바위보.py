import random
import game_emoji

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
player = int(input("choose here: "))
com = random.randint(0, 2)
weapon = [game_emoji.rock, game_emoji.paper, game_emoji.scissors]

if(player >= 3 or player < 0):
  print("Your typed an invalid number, you lose!")
else:
  print(weapon[player])
  print(f"Computer chose:\n{weapon[com]}")

  if (player == 0 and com == 1) or (player == 1 and com == 2) or (player == 2 and com == 0):
    print("You lose")
  elif (player == com):
    print("Draw")
  else:
    print("You Win! Congratulation")