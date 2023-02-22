# Pick your own story game
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

playing = input("Are you sure you want to go on this adventure? ")

if playing.lower() != 'yes':
    print("\nNo problem. Bye!\n")
    quit()

answer = input(
    "You are on your car on a dirt road, it has come to an end and you can go left or right, which one do you choose? ").lower()

if answer == 'left':
    print("You come to a river, it doesn't look so deeep, but there's no way for you to know if it's safe for the car. You can try crossing it with your car or you can grab a couple of things and crossing it swimming since it's not that long.")
    answer = input("Type car for crossing with your car or swim for doing it swimming: ").lower()
    if answer == 'car':
        print("The path was inadequate for the car, it was very deep so now the car is damaged because of the water. While you were trying to take your thinks out, you were eaten by an alligator. Sorry you lose.")
    elif answer == 'swim':
        print("You were able to cross the river but now you are tired and thirsty. You don't have enough water. You find a cabin after crossing the river where you could fill your bottle of water and have some rest. The cabin has its door closed but a window where you fit opened, you knocked and no one answered.")
        answer = input("Would you go inside to refill your bottle and have some rest before continuing? Type yes for getting inside using the open window or no for walking away: ").lower()
        if answer == 'yes':
            print("You went inside and filled your bottle and had some rest. The owner of the cabin is a cop, they found you and took you to jail for getting inside without permission. You lose.")
        elif answer == 'no':
            print("You walked for many miles, you didn't find anyone else to help you and ran out of water. You couldn't make it anymoredfsd. You lost the game.")
        else:
            print("That's not a valid choice. You lose.")
    else:
        print("That's not a valid choice. You lose.")
elif answer == 'right':
    answer = input("You come to a bridge,  it looks wobbly. Do you want to cross it or head back? Type cross or back: ").lower()
    if answer == 'back':
            print("You went back and when going left you were eaten by the alligators. You lost the game.")
    elif answer == 'cross':
        print("You crossed by the bridge, and at the very end you met a stranger. They know the zone pretty well so they helped you to recover your car and you won the game. Congratulations!")
    else:
        print("That's not a valid choice. You lose.")

else:
    print("That's not a valid choice. You lose.")

print("Thank you for trying,", name)
