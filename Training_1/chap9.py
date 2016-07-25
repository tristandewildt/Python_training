'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math
from xlwt.antlr import ifelse
from tabulate import tabulate
from cmd import PROMPT


fin = open('words.txt')

#line=fin.readline()
#word = line.strip()
#print(word)
def count_words20():
    words20 = 0
    for line in fin:
        word = line.strip()
        i = 0
        amount_letters = 0
        for i in word:
            if i != " ":
                amount_letters = amount_letters + 1
        if amount_letters >= 20:
            words20 = words20 + 1
    return words20
#print(count_words20())

def word_without_e(string):
    no_e = 0
    for line in fin:
        if has_no_gl(line, string) == True:
            stript=line.strip()
            #print(stript)
            no_e = no_e + 1
    return no_e

def has_no_gl(a, string):
    letter = 0
    for letter in string:
        i = 0
        for i in a:
            if i ==str(letter):
                return False
    return True

def avoid(string):
    r = word_without_e(string)
    return r

#print('Give me a string: \n')
#re = raw_input()
#print(avoid(re))

#print('Please give word:\n')
#word=raw_input()
#print(has_no_e(word))

#print(word_without_e())

def main():
    numb = 100000
    max = 999999
    while numb <= max:
        test1 = check_4_end_pal(numb)
        if test1 == True:
            numb2 = numb + 1
            test2 = check_5_end_pal(numb2)
            if test2 == True:
                numb3 = numb2 + 1
                test3 = check_4_middle_pal(numb3)
                if test3 == True:
                    numb4 = numb3 + 1
                    test4 = check_6_pal(numb4)
                    if test4 == True:
                        print("A solution is: " + str(numb) + ", " + str(numb2) + ", "+ str(numb3)+ ", "+ str(numb4))
        numb = numb + 1
    x = "No more solutions found"
    return x

def translate_str(numb):
    number_string = str(numb)
    return number_string

def check_4_end_pal(numb):
    numby = translate_str(numb)
    if numby[2]==numby[5] and numby[3]==numby[4]:
        return True
    else:
        return False
    
def check_5_end_pal(numb):
    numby = translate_str(numb)
    if numby[1]==numby[5] and numby[2]==numby[4]:
        return True
    else:
        return False

def check_4_middle_pal(numb):
    numby = translate_str(numb)
    if numby[1]==numby[4] and numby[2]==numby[3]:
        return True
    else:
        return False

def check_6_pal(numb):
    numby = translate_str(numb)
    if numby[0]==numby[5] and numby[1]==numby[4] and numby[2]==numby[3]:
        return True
    else:
        return False
       
 
print(main())