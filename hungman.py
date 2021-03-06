from replit import clear

import random
from word import word_list
from stage import stages , logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(logo)
end_of_game = False
lives = 6


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
    
    if guess in display:
      print(f"you have already gussed {guess}")

    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
        
        lives -= 1
        print(f"letter {guess} was not in chosen_word and you lost one life")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")

   
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(stages[lives])