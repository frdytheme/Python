import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
life = 6
solution = []

for letter in chosen_word:
  solution += "_"

end_of_game = False

while not end_of_game:

  guess = input("Guess a letter: ").lower()

  if guess not in chosen_word:
    life -= 1
    if life == 0:
      end_of_game = True
      print("Game Over")

  for idx in range(len(solution)):
    if guess == chosen_word[idx]:
      solution[idx] = guess


  print(solution)

  if "_" not in solution:
    end_of_game = True
    print("추카추카")
  
  print(stages[life])

