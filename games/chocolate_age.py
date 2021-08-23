#!/usr/bin/env python3

# I remembered this old email puzzle that was passed around about in the
# mid-aughts, and I thought I'd recreated it for the kids
# steps based on those reported here: http://www.murderousmaths.co.uk/games/choc/agebychoc.htm

# Date: Sun Aug 22 09:18:31 PM EDT 2021

import os
import time
import datetime

os.system('clear')

def week():
    # ask how many chocolates per week they want
    new_line = '\n'

    while True:
        try:
            print(f"You may have from 1 to 9 chocolates per week.{new_line}")
            chocolates = int(input("How many would you like? "))
            if chocolates >= 1 and chocolates <= 9:
                return chocolates
            else:
                print("Must be a number from 1 to 9. Try again.")
        except (ValueError):
            print("Must be a number from 1 to 9. Try again.")

def first_steps():
    # these steps apply regardless of any input from user 
    new_line = '\n'

    chocolates = week()

    print(f"{new_line}Multiplying {chocolates} by 2 ...{new_line}")
    time.sleep(1) ; print(".") ; time.sleep(1) ; print(".")
    chocolates = chocolates * 2
    print(f"And the result is {chocolates}.{new_line}")

    print(f"Now adding 5 to {chocolates} ...{new_line}")
    time.sleep(1) ; print(".") ; time.sleep(1) ; print(".")
    chocolates = chocolates + 5
    print(f"And the result is {chocolates}.{new_line}")

    print(f"Next I am multiplying {chocolates} by 50 ...{new_line}")
    time.sleep(1) ; print(".") ; time.sleep(1) ; print(".")
    chocolates = chocolates * 50
    print(f"And the result is {chocolates}.{new_line}")

    return chocolates

def birth():
    # get birthyear
    while True:
        try:
            birthyear = int(input("What year were you born? "))
            time.sleep(1)   
            if birthyear >= 1922 and birthyear <= 2020:
                return birthyear 
            else:
                print("Must be a four digit number from 1922 to 2020. Try again.")
        except (ValueError):
            print("Must be a four digit number from 1922 to 2020. Try again.")

def the_year():
    # just set the current year
    new_line = '\n'
    year = datetime.datetime.today().year
    return year

def had_birthday():
    # ask if had birthday and then perform steps based on current year and if
    # had birthday
    new_line = '\n'
    chocolates = first_steps()
    year = the_year()

    while True:
        try:
            answer = input("Have you had a birthday this year? (y/n) ")
            if answer == "y" and year == 2021:
                print(f"Then I will add 1771 to {chocolates} ...{new_line}")
                time.sleep(1) ; print(".") ; time.sleep(1) ; print(".")
                chocolates = chocolates + 1771
                return chocolates
            elif answer == "n" and year == 2021:
                print(f"Then I will add 1770 to {chocolates} ...{new_line}")
                time.sleep(1) ; print(".") ; time.sleep(1) ; print(".")
                chocolates = chocolates + 1770
                return chocolates
            elif answer == "y" and year == 2022:
                print(f"Then I will add 1772 to {chocolates} ...{new_line}")
                time.sleep(1) ; print(".") ; time.sleep(1) ; print(".")
                chocolates = chocolates + 1772
                return chocolates
            elif answer == "n" and year == 2022:
                print(f"Then I will add 1771 to {chocolates} ...{new_line}")
                time.sleep(1) ; print(".") ; time.sleep(1) ; print(".")
                chocolates = chocolates + 1771
                return chocolates
            elif answer == "y" and year > 2022:
                print(f"Then I will add 1770 to {chocolates} ...{new_line}")
                time.sleep(1) ; print(".") ; time.sleep(1) ; print(".")
                chocolates = chocolates + 1770
                return chocolates
            elif answer == "n" and year > 2022:
                print(f"Then I will add 1769 to {chocolates} ...{new_line}")
                time.sleep(1) ; print(".") ; time.sleep(1) ; print(".")
                chocolates = chocolates + 1769
                return chocolates
            else:
                print("Must enter 'y' or 'no'. Try again.")
        except (SyntaxError):
            print("Must enter 'y' or 'no'. Try again.")

def completion():
    # finish up
    new_line = '\n'
    chocolates = had_birthday()
    birthyear = birth()

    chocolates = chocolates - birthyear

    print(f"{new_line}The first digit is the number of chocolates you chose{new_line}.")
    print(f"The last two digits are your age. {new_line}")
    print(chocolates)
    print(f"{new_line}")

if __name__ == '__main__':
    completion()
