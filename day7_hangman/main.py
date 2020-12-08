#Step 4

import random
import word_list
import hangman_logo
from replit import clear

end_of_game = False
#word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list.word_list)
word_length = len(chosen_word)

passado=[]

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
lives = 6

display = []
for _ in range(word_length):
    display += "_"
print(f"welcome to hangman {hangman_logo.logo}")
while not end_of_game:
    guess = input(f"Guess a letter,you have {lives} lives: ").lower()
    if guess not in passado:
        passado+=guess
    else:
        print("letter already used")
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if letter != guess:
            lives -= 1


    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if lives==6:
        clear()
        print(f"{hangman_logo.stages[6]}")
    elif lives ==5:
        clear()
        print(f"{hangman_logo.stages[5]}")
    elif lives ==4:
        clear()
        print(f"{hangman_logo.stages[4]}")
    elif lives ==3:
        clear()
        print(f"{hangman_logo.stages[3]}")
    elif lives ==2:
        clear()
        print(f"{hangman_logo.stages[2]}")
    elif lives== 1:
        clear()
        print(f"{hangman_logo.stages[1]}")
    elif lives <= 0:
        clear()
        end_of_game = True
        print(f"loose {hangman_logo.stages[0]}")
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
