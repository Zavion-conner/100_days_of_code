import random
# from hangmanwrd import stages
from hangmanwrd  import word_list
chosen_word = random.choice(word_list)

lives = 6
from hangmanwrd import logo
print(logo)
word_length = len(chosen_word)
print(f"the word is {chosen_word}")
display = []
for letter in chosen_word:
    display += "_"


end_of_game = False
while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    for position  in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position} \n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter
    
    if   guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1 
        if lives == 0: 
              end_of_game = True
              print ("You lose!")
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    from hangmanwrd import stages
    print(stages[lives])