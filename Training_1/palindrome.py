'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math
from xlwt.antlr import ifelse



def is_palindrome(word):
    x = check_length(word)
    if x == 1:
        return
    else:
        long_enough(word)


def check_length(word):
    if len(word) < 2:
        print('Word is not long enough')
        return 1

def long_enough(word):
    if len(word) < 2:
        print('Palindrome!')
        return None
    elif len(word) >= 2:
        if first(word) == last(word):
            word = middle(word)
            return long_enough(word)
        else:
            print('Not a palindrome')
            return None

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
    
is_palindrome('op')








