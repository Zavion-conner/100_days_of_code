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
lives = 6
chosen_word = random.choice(word_list)
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
            # print(f"Current position: {position} \n Current letter: {letter}\n Guessed letter: {guess}")= see postion for debugging
            if letter == guess:
                display[position] = letter
    
    if   guess not in chosen_word:
         lives -= 1 
         if lives == 0: 
              end_of_game = True
              print ("You lose!")
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives])