'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math
from xlwt.antlr import ifelse
from tabulate import tabulate
from sympy.core.numbers import NumberSymbol
from _ast import Str


eng2sp = dict()
#eng2sp['one'] = 'uno'
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

#print(eng2sp)
#print('one' in eng2sp)

vals = eng2sp.values()
#print('uno' in vals)


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram('blablacadabratesque')
#print(h)
#print(h.get('b'))


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

#print(reverse_lookup(h, 2))



def reverse_lookup_list(d, v):
    rlist =[]
    for k in d:
        if d[k] == v:
            rlist.append(k)
    if rlist == []:
        raise LookupError()
    return rlist

#print(reverse_lookup(h, 3))



def fibonacci_old (n):
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci_old(n-1) + fibonacci_old(n-2)
    
known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

#print(fibonacci(60))


count = 0

def example():
    global count
    count += 1
    return count

known = {0:0, 1:1}

def example2():
    known[2] = 1
    return known

#print(example2())

#
fin = open('words.txt')
def set_dic():
    take = dict()
    #n=1
    for line in fin:
        take[line.strip()] = 0
        #n += 1
    return take

#print(set_dic())

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

#print (h)
#print(invert_dict(h))


def invert_dict2(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

#print(invert_dict2(h))

liste = (10, 17, 12, 13, 10)

def takelasts(word, x):
    return word[x]

#    print('Lastletter in takelasts is: ' + word[-1] + '.')
    
 

def has_duplicates(h):
    ref = dict()
    for n in h:
        if n in ref:
            return True
        ref[n] = True
        #print(ref)
    return False

#print(has_duplicates(liste))

#print(has_duplicates(liste))


#newlist = ('pupu', 'yuyu', 'upup')
#print(newlist)
#print(ord(''))

def rotate_pairs():
    result = dict()
    with open('words.txt', 'r') as fin:
        for line in fin:
            y = check_word_to_list(line.strip())
            if y != None:
                result.setdefault(line.strip(),[line.strip()])
                result[line.strip()].append(y)
        return result 


def check_word_to_list(line):
    with open('words2.txt', 'r') as fin2:
        for line2 in fin2:
            x = check_word_to_word(line, line2.strip())
            if x == True:
                return line2.strip()
            else:
                return
     

def check_word_to_word(line, line2):
    
#    print('check')
    
    if len(line.strip()) == len(line2.strip()):
        
        lastletter = - 1
        #works
#        print('check2')
#        print(line)
#        print('line 2 is: ' + line2)

        
        for letter in line:
            z = takelasts(line2.strip(), lastletter)
#            print(z)
#            print(lastletter)
#            print(z)
#            print(letter)
#            print('Lastletter is' + z + '.')
            if letter != z:
                return False
            else:
                lastletter =- 1 
        print('ja')        
        return True


#fin2 = open('words2.txt')


print(rotate_pairs())


#work = 'chaton'
#print(work[-2])

#print(rotate_pairs())                
                
       
                
                
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]









