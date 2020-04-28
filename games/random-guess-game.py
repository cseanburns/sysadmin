#!/usr/bin/python3

# Random Number Guessing Game
# by Sean Burns
# Guess a number between 1 and 100
# Creation: Wed 12 Dec 2018 
# Revision: Tue Apr 28 00:09:18 EDT 2020
#
# To do:
# Track score history
# Tell players how many guesses it took to get the correct guess
# Generate a plot (pyplot) plotting each random number as they play
 
import os
import random
from colorama import Fore

def playgame():
    # Clear screen
    os.system('clear')
    
    # Get a random number
    x = random.randrange(1, 100, 1)
    
    # Ask user for input
    print("Guess a number from 1 to 100.")
    guess = input("Please enter your number: ")
    
    # If first guess is correct
    if (int(guess) == x):
        print(Fore.MAGENTA + "Are you psychic, because you guessed right away!")

    # If first guess is not correct
    while (int(guess) != x):
        if (int(guess) > x):
            print(Fore.RED + "Your guess is too high.")
            guess = input(Fore.WHITE + "Guess again: ")
            if (int(guess) == x):
                print(Fore.BLUE + "Congratulations, that is correct!")
        elif (int(guess) < x):
            print(Fore.GREEN + "Your guess is too low.")
            guess = input(Fore.WHITE + "Guess again: ")
            if (int(guess) == x):
                print(Fore.BLUE + "Congratulations, that is correct!")
                print(Fore.WHITE)
        else:
            print(Fore.WHITE + "Game over.")

# code below modified from:
# https://stackoverflow.com/questions/19554982/exit-a-program-conditional-on-input-python-2

def playagain():
    while True:
        replay = input(Fore.WHITE + "Play again? Enter y or n. ").lower()

        if replay in ("yes", "y"):
            playgame()
        elif replay in ("no", "n"):
            print("Thank you for playing.")
            raise SystemExit
        else:
            print(Fore.RED + "Sorry, I don't understand.")

def main():
    playgame()
    playagain()
    
if __name__ == '__main__':
    main()
