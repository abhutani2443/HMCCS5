# coding: utf-8
#
# hw0pr2b.py
#

""" 
Title for your adventure:   Rocket Quest.

Notes on how to "win" or "lose" this adventure:
  To win: 'start the ship/find a fueling station/cry', 'through', 'follower', 'sent out into space', 'yes' 
  To lose: any other choice.

"""
import os
import time
delay = 2
def adventure():
    username = input("What do they call you, worthy space adventurer? ")

    print()
    print("Welcome,", username, "to the SpaceZ exoplanet explorer, the most advanced rocket ever known to man.")
    print()

    print("Your quest: To find a new home, because you, yes you, have destroyed the planet.")
    print()
    idk = input("What would you like to do? (start the ship, find a fueling station, stay put, cry): ")
    print()
    if (idk == "start the ship"):
        print("Running low on fuel...but you'll make it.")
    elif (idk == "find a fueling station"):
        print("Wise choice! No chance of getting stranded now.")
    elif(idk == "stay put"):
        print("Nooooo, aliens have taken over ship! YOU LOSE!")
        print("Farewell,", username)
        os._exit(1)
    else:
        print("Good choice, let's keep going.")
    
    print()
    print("You see a potential planet to inhabit.")
    print("You can either fly around the astroid belt, losing most of your fuel, or through, conserving your fuel...")
    time.sleep(delay)
    print()

    choice1 = input("Do you choose to go through or around? ")
    print()

    if choice1 == "through":
        print("You made the right choice, now landing...")
        time.sleep(delay)
        print("You're a smarty,", username+"!")

    else:  
        print("OH NO! You're stranded in space. TOO BAD :(")
        print("Bye now!")
        os._exit(1)
    print()

    print("You land on the planet...")
    time.sleep(delay)
    print()
    print("You see a strange figure come up to you...woah it speaks English!")
    print("Alien: Hello, who are you and why are you on this planet?")
    time.sleep(delay)
    print()
    what = input("What are you going to respond? (conquerer, follower) ")
    print()
    if(what == 'conquerer'):
        print("Sorry! The alien race has knocked you out, Good Bye! :)")
        os._exit(1)
    elif(what == 'Follower'):
        print("Good choice! The aliens are much more advanced than you and would have wiped you out if you chose to conquer.")


    print("The aliens start to show you around the planet...")
    time.sleep(delay)
    print("You notice the extremely advanced infrastructure.")
    print("The aliens give you three choices: join the society, live as a prisoner, or be sent out into space.")
    time.sleep(delay)
    print()
    next = input("What are you going to do? ")
    
    print()
    
    if(next == 'join the society'):
        print("They actually just keep you captive! Bye Bye")
        os._exit(1)
    elif(next == 'live as a prisoner'):
        print("ok, obviously you lose.")
        print("bye")
        os._exit(1)
    else:
        print("The aliens like your daring spirit, they let you stay.")
    print()
    time.sleep(delay)
    decision = input("Do you accept the invitation to stay? (yes, no) ")

    if(decision == 'yes'):
        print("Heyyyyy, you win buddy!")
    
    if(decision == 'no'):
        print("Well, ok, you lose then.")
