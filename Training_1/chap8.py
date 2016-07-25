'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math
from xlwt.antlr import ifelse
from tabulate import tabulate



letter = 0
fruit = 'banata'
#for letter in fruit:
#    print(letter)

#print(fruit[:])

greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
print(find(fruit,'t'))

new_word = fruit.upper()
print(new_word)













