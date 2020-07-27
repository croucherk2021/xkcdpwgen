#!/usr/bin/env python

import argparse
import random
import string

# command line argument parser w/ argument parameters
parser = argparse.ArgumentParser(prog='xkcdpwgen', conflict_handler='resolve')
parser.add_argument('-w', '--words', help='include WORDS words in the password (default=4)',
                    action="store", type=int, default=4)
parser.add_argument('-c', '--caps', help='capitalize the first letter of CAPS random words (default=0)',
                    action="store", type=int, default=0)
parser.add_argument('-n', '--numbers', help='insert NUMBERS random numbers in the password (default=0)',
                    action="store", type=int, default=0)
parser.add_argument('-s', '--symbols', help='insert SYMBOLS random numbers in the password (default=0)',
                    action="store", type=int, default=0)
args = parser.parse_args()

def choices(population, k):
    total = len(population)
    return [population[int(random() * total)] for i in range(k)]

# function to produce pw given 4 count variables
def word_pw(w, c, n, s):
    pw = ''
    words = []
    file = open('corncob_lowercase.txt').read().splitlines()
    
    for x in range(w):
        word = random.choice(file)
        words.append(word)

    if c > w:
        c = w
        print("cap value set to words value; enter a cap value <= to words value")
    
    for y in range(c):
        words[y] = words[y].capitalize()

    nums = ''
    for i in range(n):
        num = random.choice(string.digits)
        nums = nums + num

    syms = ''
    for j in range(s):
        sym = random.choice(string.punctuation)
        syms = syms + sym

    chars = nums + syms

    for char in chars:
        words.append(char)

    random.shuffle(words)

    for word in words:
        pw = pw + word

    return pw

# call to pw generator, at default the call is word_pw(4, 0, 0, 0)
pw = word_pw(args.words, args.caps, args.numbers, args.symbols)
print(pw)



