'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math, operator
import os
import dbm
import pickle
from xlwt.antlr import ifelse
from tabulate import tabulate
from sympy.core.numbers import NumberSymbol
from _ast import Str


camels = 52
appels = 48
hamburgers = 3
#print('The are %d camels %s here eating %d appels and %d hamburgers.' % (camels, 'walking', appels, hamburgers))

# %d is to format an integer, %g to format a floating-point numbers and %s to format a string 

cwd = os.getcwd()
#print(cwd)

#print(os.path.abspath('New3.py'))
#print(os.path.exists('New3.py'))
#print(os.path.isdir('D:\Workspace\Python_training\Training_1'))

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

#walk('D:\Workspace\Python_training')

# The following structure is use to ensure the program can go on even if something went wrong.
def tentative():
    try:
        fin = open('words3.txt')
    except:
        print('Something went wrong, could not open the file.')

#tentative()

# This is to open a database, or create one if it does not exist. Keys and values of a table have to be string or bytes.
def write_and_print(a, b):
    db = dbm.open('captions', 'c')
    db[a]=b
    for key in db:
        print(key, db[key])
    db.close()

pile = 4
face = 8
#write_and_print(str(pile), str(face))

# As only strings and bytes can be inserted in databases, pickles can help as it changes every object to strings.
t= [1,5,8]
#print(pickle.dumps(t))
# and just ot visualize the string again, you use pickle.loads
s = pickle.dumps(t)
t2 = pickle.loads(s)
#print(t2)
# Note that t is t2 would then be considered as false (not the same object)
#print(t is t2)

#cmd = 'ls -l'
#fp = os.popen(cmd)
#res = fp.read()
#stat = fp.close()
#print(stat)

#filename = 'de_wildt_phd_literature_review_3.tex'
#cmd = 'md5sum ' + filename
#fp = os.popen(cmd)
#res = fp.read()
#stat = fp.close()
#print(res)
#print(stat)

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

#print(linecount('words.txt'))

#if __name__ == '__main__': #if the program is running as a script, __name_ has the value '__main__'. If the module is being imported, the test code is skipped.
#    print(linecount('words.txt'))

s = '1 2\t 3\n 4'
#print(s)
#print(repr(s))

def sed(pat_string, repl_string, file1, file2):
    try:
        fin = open(file1)
    except:
        print('Something went wrong, could not open the file.')
        return
    
    temp = []
    for line in fin:
        print(line)
        print(pat_string)
        if str(line) == str(pat_string):
            line == repl_string
        temp.append(line.strip())
    fin.close
    
    db = dbm.open(file2, 'c')
    for value in temp:
        db[value]= str(1)
    db.close()
    
    
    #return temp

pat_string = 'Lilili'

repl_string = 'Lululu'

file1 = 'file1.txt'
file2 = 'replaced.' + file1 
#sed(pat_string, repl_string, file1, file2)

"""
# Improved code is
"""
def main():
    pat_string2 = 'Lilili'
    repl_string2 = 'Lululu'
    file3 = 'file1.txt'
    file4 = 'replaced.' + file1 
    sed2(pat_string2, repl_string2, file3, file4)

def sed2(pat_string, repl_string, file1, file2):
    fin = open(file1, 'r')
    dump = open(file2, 'w')
    for line in fin:
        line = line.replace(pat_string, repl_string)
        dump.write(line)
    fin.close()
    dump.close()
#main()

""" 
Exercise 14-2
"""

def exo14_2():
    from chap12 import search_anagrams
    x = search_anagrams()
    print(x)
exo14_2()

