import hangman_art
import hangman_words
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

chosen_word = random.choice(hangman_words.word_list)

display = []

for letter in chosen_word:
  display += "_"

print(hangman_art.logo)
print(f"Pssst, the solution is {chosen_word}.")
end_of_games = False
life = 6
while not end_of_games:
  guess = input("Guess a letter: ").lower()

  clear()

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    life -= 1
    if life == 0:
      end_of_games = True
      print("Game Over")
  else:
    for idx in range(len(display)):
      if guess == chosen_word[idx]:
        display[idx] = guess
  
  print(' '.join(display))
  
  if "_" not in display:
    end_of_games = True
    print("추카추카")
  
  print(hangman_art.stages[life])