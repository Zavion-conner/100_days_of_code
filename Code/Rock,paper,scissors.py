# Rock paper scissors 
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Use the rock paper scissor variables above to make list 
rpc = [rock,paper, scissors ]
# Have the user select their desired input 
User_imp = int(input("Rock'0', paper'1' or scissors'2' "))
# print the users choice(just the number)
print(f"You chose: \n{User_imp}")
# if the user enters a number more than 2 or less than 0 display an error message 
if User_imp >= 3 or User_imp < 0:
    print("You typed an invaild number")
    # (all statments after this are indented to continue the code after a the users input has been verified preventing index error )
else:
    print(rpc[User_imp])
    # user input decides the image that will be shown
    computer_choice = int(random.randint(0,2))
# print the computer choice along with the corresponding image
    print("The computer chose:")
    print(rpc[computer_choice])
    # if user chooses rock and the computer chooses scissors than the user wins 
    if User_imp == 0 and computer_choice == 2:
        print("User wins")
    # if the computer chooses rock and the user chooses scissors than the computer wins 
    elif computer_choice ==0 and User_imp == 2:
        print("computer wins")
    # if the user input is greater than the computer input than the user will. this will exculed user == 0 and comp == 2 because that state occured before this one
    elif User_imp > computer_choice:
        print("You win!")
    elif computer_choice > User_imp:  
        print("computer wins!")
    elif User_imp == computer_choice:
        print("It is a draw game")
