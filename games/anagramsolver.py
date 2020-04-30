#!/usr/bin/env python3 

# Anagram solver, by Sean Burns

# 1. Take as input a series of scrambled letters.
#
# 2. Take as input a single letter that is required in the output
#
# 3. Take as input an integer that determines how many characters per
# word (ex: 4 for four letter words, 5 for five letter words, etc.), but
# be warned, values too high are computationally expensive and may crash
# computer
#
# 4. Compare output to a list of words (file named 'wordlist'). The word
# list is based on the american-english dictionary located at
# /usr/share/dict/american-english. The dictionary file was cleaned up
# with Bash (removed punctuations, lower cased, etc) and the file was
# renamed to 'wordlist'

# To Do: Create if statements to exit nicely if input is not understood
# To Do: Don't ask to re-enter letters and mainletter
# To Do: Print output in pretty columns
# To Do: Make 'main letter' optional so that it could just be an anagram
# solver and not just a NYTimes Spelling Bee solver

import os
import re
import sys
from itertools import product
 
os.system('clear')

def scrambledletters():
    print("Enter letters: ")
    letters = input()
    letters = str(letters.lower())
    return letters

def centerletter():
    print("Enter center letter: ")
    letter = input()
    letter = str(letter.lower())
    return letter

def wordlength():
    print("Enter length of words (>= 4 | <=8): ")
    repeats = input()
    repeats = int(repeats)
    return repeats

def formwords():
    letters = scrambledletters()
    mainletter = centerletter()

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
    while True:
        formwords()

def main():
    newnumber()
    
if __name__ == '__main__':
    main()
