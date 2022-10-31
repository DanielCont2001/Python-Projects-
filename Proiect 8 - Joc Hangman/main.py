
import random
from turtle import clear
from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo

print(logo)

display = []
for _ in range(word_length):
    display += "_"
  
while not end_of_game:
    guess = input("Introdu o litera: ").lower()

    clear()
    if guess in display:
      print(f"Deja ai ghicit litera {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Litera {guess} nu este in cuvant, ai pierdut o viata.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Ai pierdut.")
      
    print(f"{' '.join(display)}")
    

    if "_" not in display:
        end_of_game = True
        print("Ai castigat.")
      
    print(stages[lives])