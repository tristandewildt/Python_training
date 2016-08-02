'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math, operator
from xlwt.antlr import ifelse
from tabulate import tabulate
from sympy.core.numbers import NumberSymbol
from _ast import Str


#print((0, 1, 2) < (0, 3, 4))            
 
a = 1
b = 2

a,b=b,a
#print(a), print(b)

addr = 'monty@python.org'
uname, domain = addr.split('@')

#print(uname), print(domain)

quot, rem = divmod(7, 3)
#print(quot), print(rem)

def return_tuple(a, b):
    quot, rem = divmod(a, b)
    return quot, rem

#print(return_tuple(15,4))

t=(48,7)

#print(divmod(*t)) # * is used to cope with variable-length arguments tuples

def sumall(y):
    return sum(y)

y=(47,45,1,45, 4)
#print(sumall(y))

s = 'abc'
t = [0, 1, 2]
r = 'joh' 
#print(zip(s, t))

#for l in zip(s,t,r):
#    print(l)

#ru = (list(zip(s, t)))
#for s, t in ru:
#    print(s,t)


tuple1 = (2,5,8)
tuple2 = (8,5,7)

def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

#print(has_match(tuple1, tuple2))

#for index, element in enumerate('abc'):
#    print(index, element)

d = {'a':0, 'b':1, 'c':2}
t = d.items()
#print(t)

t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)
#print(d)

# to create a dictionary:
d = dict(zip('abc', range(3)))
#print(d)

def most_frequent(text):
    dico = dict()
    for l in text:
        if l not in dico:
            dico[l]=1
        else:
            dico[l]+= 1   
    sorted_dico = sorted(dico.items(), key=operator.itemgetter(1),reverse=True)
    return sorted_dico     

text = 'abcabeaft'

#print(most_frequent(text))


def search_anagrams_temp():
    dico = dict()
    with open('words.txt', 'r') as fin:
        for worda in fin:
            word1=worda.strip()
            if word1 not in dico: #check
                with open('words.txt', 'r') as fin2:
                    for wordy in fin2:
                        word2 = wordy.strip()
                        if len(word2) == len(word1):
                            x = check_anagram_temp(word1, word2)
                            if x == True:
                                if word1 not in dico:
                                    dico[word1]=[word2]
                                else:
                                    dico[word1].append(word2)
            
    return dico
                

def check_anagram_temp(word1, word2):
    for letter in word1:
        if letter not in word2:
            return False
    for lettar in word2:
        if lettar not in word1:
            return False
    return True

#print(search_anagrams_temp())

fin = open('words.txt')

def search_anagrams():
    dico = {}
    for line in fin:
        word = line.strip().lower()
        x = order(word)
        if x not in dico:
            dico[x] = [word]
        else:
            dico[x].append(word)
    dico = filter_length(dico)
    return dico

def filter_length(dico):
    dico2 = {}
    for word, anagrams in dico.items():
        if len(anagrams)>1:
            dico2[word] = anagrams
    return dico2

def order(word):
    t= list(word)
    t.sort()
    t = ''.join(t)
    return t
    
print(search_anagrams())





































