#Did not use starter code, so may look a little different

# CS5 Gold/Black: HW 0, Problem 2a
# Filename: hw0pr2a.py
# Name: Arpita Bhutani
# Problem description: RPSLS

import random

while True:

    num = int(random.uniform(0,5))

    print("Let's play a game of rock, paper, scissors, lizard, spock!")
    print("Type your weapon here and press enter:")
    user = input()
    print()

    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    if(choices[num] == user):
        print("Your Weapon: ", user)
        print("My Weapon: ", choices[num])
        print("Nooo! We tied")
    elif ((choices[num] == 'rock' and (user != 'paper' and user != 'spock'))
        or (choices[num] == 'paper' and (user != 'scissors' and user != 'lizard'))
        or (choices[num] == 'scissors' and (user != 'rock' and user != 'spock'))
        or (choices[num] == 'lizard' and (user != 'scissors' and user != 'rock'))
        or (choices[num] == 'spock' and (user != 'paper' and user != 'lizard'))):
        print("Your Weapon: ", user)
        print("My Weapon: ", choices[num])
        print("Haha! You lose, surrender to the computer.")
    else:
        print("Your Weapon: ", user)
        print("My Weapon: ", choices[num])
        print("Awww dang, you win. I'll get ya next time!")

    response = input("Play again? (yes or no): ")
    print()
    if response == 'no':
        break