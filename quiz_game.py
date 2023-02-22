#Quiz game
print("\nWelcome to the Quiz Game! \n")

playing = input("Do you want to play this game? ")


if playing.lower() != 'yes':
    print("\nOkay. Bye!\n")
    quit()

print("\nLet's play :) \n")
score = 0


#Question 1
answer = input("How many legs does a spider have? ")
print()

if answer.lower() == "8" or answer.lower() == "eight":
    print("Congratulations! Your answer is correct!")
    score += 1
    print("Your score is:", score, "\n")
else:
    print("Incorrect! The answer is 8")
    print("Your score is:", score, "\n")

#Question 2
answer = input("How many pairs of wings do bees have? ")
print()

if answer.lower() == "2" or answer.lower() == "two":
    print("Congratulations! Your answer is correct!")
    score += 1
    print("Your score is:", score, "\n")
else:
    print("Incorrect! The answer is 2")
    print("Your score is:", score, "\n")

#Question 3
answer = input("How many days are in a year? ")
print()

if answer == "365":
    print("Congratulations! Your answer is correct!")
    score += 1
    print("Your score is:", score, "\n")
else:
    print("Incorrect! The answer is 365")
    print("Your score is:", score, "\n")

#Question 4
answer = input("How many planets are in our solar system? ")
print()

if answer.lower() == "8" or answer.lower() == "eight":
    print("Congratulations! Your answer is correct!")
    score += 1
    print("Your score is:", score, "\n")
else:
    print("Incorrect! The answer is 8")
    print("Your score is:", score, "\n")

#Question 5
answer = input("Which Disney movie is Elsa in? ")
print()

if answer.lower() == "frozen":
    print("Congratulations! Your answer is correct!")
    score += 1
    print("Your score is:", score, "\n")
else:
    print("Incorrect! The answer is Frozen")
    print("Your score is:", score, "\n")

#Results
print("Your final score is:", score)
print("You got a " + str((score/5)*100) + "%\n")

print("Thank you for playing! :D \n")