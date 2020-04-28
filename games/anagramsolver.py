#!/usr/bin/python3 

# Started on:   Date: Thu Jan  2 00:12:57 EST 2020
# Revisited on: Date: Mon Apr 27 00:31:27 EDT 2020
# Revised:      Date: Mon Apr 27 17:12:12 EDT 2020
#
# To Do:
# 1. print only those matches that have the essential letter in the
# anagram. For example, the NY Times Spelling Bee game requires one
# specific letter in all found words
# 2. check data input strings are strings, integers are integers

# sys is for inputing integers and product is for creating letter
# combinations
import sys
from itertools import product

# Take as input some scrambled letters and then ask for length of word
# formations. On my laptop, going past 8 is too computationally
# demanding, so warn against that.
#
# Compare to a wordlist: based on the american-english dictionary
# located at /usr/share/dict/american-english.
#
# The dictionary file has been cleaned up in Bash (removed punctuations,
# lower cased, etc) and the file was renamed as 'wordlist'

def scramble():
    print("Enter letters: ")
    letters = input()
    print("Enter number of repeats (no more than 8): ")
    repeats = input()
    repeats = int(repeats)
    suggestions = product(letters, repeat = repeats)
    result = []
    for i in suggestions:
        result.append(''.join(i))

    with open('wordlist', 'r') as wordlist:
        comparewords = wordlist.read().splitlines()
            
    print(*set(result).intersection(comparewords))

def main():
    scramble()

main()
