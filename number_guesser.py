#Guesser game
import random

print("\nWelcome to the Guessing Game! \n")


top_number = input("Type a number larger than 0: ")
guesses = 0

#Make sure if it's a number and if it's greater than 0
if top_number.isdigit():
    top_number = int(top_number)

    if top_number <= 0:
        print("Please type a number greater than 0 next time")
        quit()

else:
    print("Please type a number next time")
    quit()

random_number = random.randrange(0, top_number)

while True:
    guesses += 1
    guessed_number = input("Guess the random number: ")
    if guessed_number.isdigit():
        guessed_number = int(guessed_number)
    else:
        print("Please type a number next time")
        continue  #takes the program back to the beginning of the loop

    if guessed_number == top_number:
        print("\nYou guessed!! :)\n")
        print("It took you " + str(guesses) + " guesses\n")
        break
    elif guessed_number < top_number:
        print("\nSorry, that's not the number")
        print("Hint: You are below the number!\n")
    else:
        print("\nSorry, that's not the number")
        print("Hint: You are above the number!\n")
