#Rock, paper, scissors game
import random

playing = input("Do you want to play this game? ")

if playing.lower() != 'yes':
    print("\nOkay. Bye!\n")
    quit()

print("\nLet's play 2 of 3 :) \n")

options = ["rock", "paper", "scissors"]
score_player = 0
score_computer = 0  

while True:
    user_option = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_option == 'q':
        break
    
    if user_option not in options:  #Checking if the user typed down anything that's not within this list
        print("Not a valid option\n")
        continue
    
    computer_index = random.randint(0, 2)
    computer_pick = options[computer_index]

    print("\nComputer picked", computer_pick + ".")

    if user_option == 'rock' and computer_pick == 'scissors':
        print('You won!\nyes')
        score_player += 1

    elif user_option == 'paper' and computer_pick == 'rock':
        print('You won!\n')
        score_player += 1

    elif user_option == 'scissors' and computer_pick == 'paper':
        print('You won!\n')
        score_player += 1

    elif user_option == computer_pick:
        print('Oh no! We tied...\n')

    else:
        print('Computer won this point!\n')
        score_computer += 1

    if score_computer == 3:
        print("\nSorry! Computer won this game")
        break

    if score_player == 3:
        print("\nCongrats! You won this game!")
        break


print("Thank you for playing!\n")


