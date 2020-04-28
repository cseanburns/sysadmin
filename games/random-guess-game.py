#!/usr/bin/python3

# Random Number Guessing Game
# by Sean Burns
# Guess a number between 1 and 100
# Wed 12 Dec 2018 
# revision: Tue Apr 28 00:09:18 EDT 2020
#
# Ask players if they want to play again
# Track score history
# Tell players how many guesses it took to get the correct guess
# Generate a plot (pyplot) plotting each random number as they play
 
import os
import random
from colorama import Fore

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
