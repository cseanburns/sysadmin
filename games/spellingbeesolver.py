#!/usr/bin/env python3 

# NYTimes Spelling Bee solver, by Sean Burns, April 30, 2020
#
# The Spelling Bee program https://www.nytimes.com/puzzles/spelling-bee
# provides seven letters, one of which, the center, must be included.
#
# To use this script, enter the seven letters at the first prompt. In
# the second prompt, specify the required, center letter. In the
# subsequent prompts, choose *n*-length words to output. 
#
# Unless you have a particularly powerful processor and loads of memory,
# it's wise not to enter too large an *n*. My lightweight laptop will
# freeze if *n* is greater than 9.
#
# The script generates possible word formations at *n*-length words and
# then outputs those words that are found in a wordlist. The 'wordlist'
# file in this repository is therefore required to run this script.
#
# The 'wordlist' file is /usr/share/dict/american-english
# (Debian/Ubuntu). That dictionary file was cleaned up with Bash
# (punctuation removed, cases lowered, etc) and renamed to 'wordlist'.
#
# To Do: Make center letter optional so that it could just be an anagram
# solver and not just a NYTimes Spelling Bee solver.
 
import os
import re
import sys
from itertools import product
from colorama import Fore, Style
 
os.system('clear')

print("NYTimes Spelling Bee Solver\n")

print("Enter all seven letters: \n")
letters = input()
letters = str(letters.lower())

print("Specify center letter: ")
mainletter = input()
mainletter = str(mainletter.lower())

if len(letters) != 7:
    sys.exit("Bye. You must have seven letters.")
elif mainletter not in letters:
    sys.exit("Bye. Need to enter letter from those entered above.")
else:
    print("Proceed. " + Fore.RED + "Press Ctrl-C to quit.\n")

print(Fore.GREEN + "Wise not to enter more than 9 or 10\n")

def wordlength():
    print(Style.RESET_ALL + "Enter length of words: ")
    repeats = input()
    repeats = int(repeats)
    return repeats

def formwords():
    repeats = wordlength()

    # create possible word formations
    suggestions = product(letters, repeat = repeats)

    result = []
    for i in suggestions:
        result.append(''.join(i))

    # reduce possible word formations to those
    # listed in the dictionary
    with open('wordlist', 'r') as wordlist:
        comparewords = wordlist.read().splitlines()

    # reduce words to those with the main letter
    lettermatch = re.compile(".*{}".format(mainletter))
    comparewords = list(filter(lettermatch.match, comparewords))
    
    # print results
    print(*set(result).intersection(comparewords))
    print("")

def newnumber():
    formwords()

def main():
    while True:
        newnumber()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Bye!")

# This script is a product of COVID-19 quarantine. After a long day, I
# didn't want to do any more work, watch any more shows, or read
# anything, and thought I'd just play around with and practice Python.
