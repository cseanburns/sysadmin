#!/usr/bin/env python3
"""
Random Number Guessing Game
by Sean Burns
Guess a number between 1 and 1000
Wed 12 Dec 2018

TODO:
1. Track score history
2. Tell players how many guesses it took to get the correct guess
3. Generate a plot (pyplot) plotting each random number as they play
"""

import os
import random
from colorama import Fore

def playgame():
    """
    This function sets a random number, asks user for a number as an integer,
    then proceeds to ask for numbers until the guess equals the random number.
    """
    # Clear screen
    os.system('clear')

    # Get a random number
    set_random = random.randrange(1, 100, 1)

    # Ask user for input
    print("Guess a number from 1 to 100.")
    guess = input("Please enter your number: ")
    guess = int(guess)

    # If first guess is correct
    if guess == set_random:
        print(Fore.MAGENTA + "Are you psychic, because you guessed right away!")

    # If first guess is not correct
    while guess != set_random:
        if guess > set_random:
            print(Fore.RED + f"Your guess of {guess} is too high.\n")
            guess = input(Fore.WHITE + "Guess again: ")
            guess = int(guess)
            if guess == set_random:
                print(Fore.BLUE + f"Congratulations, your guess of {guess} is correct!\n")
        elif guess < set_random:
            print(Fore.GREEN + f"Your guess of {guess} is too low.\n")
            guess = input(Fore.WHITE + "Guess again: ")
            guess = int(guess)
            if guess == set_random:
                print(Fore.BLUE + f"Congratulations, your guess of {guess} is correct!\n")
                print(Fore.WHITE)
        else:
            print(Fore.WHITE + "Game over.")

# code below modified from:
# https://stackoverflow.com/questions/19554982/exit-a-program-conditional-on-input-python-2

def playagain():
    """
    This function lets user play again if they want.
    """
    while True:
        replay = input(Fore.WHITE + "Play again? Enter y or n. ").upper()

        if replay in ("Yes", "Y"):
            playgame()
        elif replay in ("No", "N"):
            print("Thank you for playing.\n")
            raise SystemExit
        else:
            print(Fore.RED + "Sorry, I don't understand.")

def main():
    """ This function allows the script to run as a standalone program."""
    playgame()
    playagain()

if __name__ == '__main__':
    main()
