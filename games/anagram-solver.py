#!/usr/bin/python3 

# Created:  Date: Thu Jan  2 00:12:57 EST 2020
# Revised: Date: Mon Apr 27 00:31:27 EDT 2020
#
# To Do:
# 1. print only those matches that have the essential letter in the
# anagram. For example, the NY Times Spelling Bee game requires one
# specific letter in all found words
# 2. Make pretty
 
from itertools import *

# take letters for anagram
letters = input()

# get cominations based on various lengths from 4 - 8 letters long
product0 = product(letters, repeat = 4)
result0 = []
for i in product0:
    result0.append(''.join(i))

product1 = product(letters, repeat = 5)
result1 = []
for i in product1:
    result1.append(''.join(i))

product2 = product(letters, repeat = 6)
result2 = []
for i in product2:
    result2.append(''.join(i))

product3 = product(letters, repeat = 7)
result3 = []
for i in product3:
    result3.append(''.join(i))

product4 = product(letters, repeat = 8)
result4 = []
for i in product4:
    result4.append(''.join(i))

# read in the word list from the american-english dictionary:
# /usr/share/dict/american-english. The file has already been cleaned up
# in Bash (punctuation removed, converted to lowercase, etc)
with open('wordlist', 'r') as wordlist:
    comparewords = wordlist.read().splitlines()

# print out the combinations of word
print(set(result0).intersection(comparewords))
print(set(result1).intersection(comparewords))
print(set(result2).intersection(comparewords))
print(set(result3).intersection(comparewords))
print(set(result4).intersection(comparewords))
