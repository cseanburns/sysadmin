#!/usr/bin/python3

# Random Number Guessing Game
# by Sean Burns
# Guess a number between 1 and 100
# Wed 12 Dec 2018 
#
# Ask players if they want to play again
# Track score history
# Tell players how many guesses it took to get the correct guess
# Generate a plot (pyplot) plotting each random number as they play
# Fix color reset after quitting/winning
 
import os
import random
from colorama import Fore

# Clear screen
os.system('clear')

# Get a random number
x = random.randrange(1, 100, 1)

# Ask user for input
print("Guess a number from 1 to 100.\n")
guess = input("Please enter your number: ")

# If first guess is correct
if (int(guess) == x):
    print(Fore.MAGENTA + "\nAre you psychic, because you guessed right away!\n")

# If first guess is not correct
while (int(guess) != x):
    if (int(guess) > x):
        print(Fore.RED + "\nYour guess is too high.\n")
        guess = input("Guess again: ")
        if (int(guess) == x):
            print(Fore.BLUE + "\nCongratulations, that is correct!\n")
    elif (int(guess) < x):
        print(Fore.GREEN + "\nYour guess is too low.\n")
        guess = input("Guess again: ")
        if (int(guess) == x):
            print(Fore.BLUE + "\nCongratulations, that is correct!\n")
            print(Fore.WHITE)
    else:
        print("Game over.\n" + Fore.WHITE)
