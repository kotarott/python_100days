# ASCII ART
print('''
    Start Treasure Island!!!
''')

print("Welcome to Treaseure Island.")
print("Your mission is to find treasure.")
choice1 = input("you're at a crossroad, where do you want to go? Type 'left' or 'right'. >>> ").lower()

if choice1 == "left":
    print("Go to next stage!")

    choice2 = input("You are in flood, what are you going to do? Type 'swim' or 'wait'. >>> ").lower()
    if choice2 == "wait":
        print("Go to next stage!")

        choice3 = input("you're in front of three doors. Which doors do you select? Type 'Red', 'Blue' or 'Yellow'. >>> ").lower()
        if choice3 == "red":
            print("Burned by fire. Game Over!")
        elif choice3 == "Blue":
            print("Eaten by beats. Game Over!")
        elif choice3 == "yellow":
            print("You win!!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout. Game Over!")
        
else:
    print("Fall into a hole. Game Over!")