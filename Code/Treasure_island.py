#Treaure Island project
print("Welcome to Treasure Island. Your mission is to find the treasure.")
direction = input("Would you like to go to the left or right. \n")
# allow the user to choose which direction they would like to go.
if direction == "left":
    sORw = input("You've came accross a river, would you like to 'swim' or 'wait'? \n")
    # Wait or swim to their death
    if sORw == "wait":
        road = input("You've came accross three roads; yellow. red and blue")
        # user picks their final path
        if road == "yellow":
             print("You win")
        elif road == "blue":
            print ("Died of illness\n GAME OVER")
        elif road == "red":
             print("Burned by fire. \n GAME OVER ")
        else:
           print("GAME OVER") 
    else:
         print("Attacked by gator.\n GAME OVER")
else: 
    print("Fall into hole and die.\n GAME OVER")