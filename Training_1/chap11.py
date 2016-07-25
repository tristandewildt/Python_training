'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math
from xlwt.antlr import ifelse
from tabulate import tabulate
from sympy.core.numbers import NumberSymbol


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
h = histogram('content')
#print(h)
#print(h.get('b'))

#def reverse_lookup(d, v):
#    for k in d:
#        if d[k] == v:
#            return k
#    raise LookupError()

def reverse_lookup(d, v):
    rlist =[]
    for k in d:
        if d[k] == v:
            rlist.append(k)
    if rlist == []:
        raise LookupError()
    return rlist

#print(reverse_lookup(h, 3))

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

#print(invert_dict(h))

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

fin = open('words.txt')

def set_dic():
    take = dict()
    n=0
    for line in fin:
        take[n] = line
        n += 1
    return take

#print(set_dic())


def invert_dict2(d):
    inverse = dict()
    for key in d:
        val = d[key]
        #print(val, key)
        inverse.setdefault(val, []).append(key)
        
        #if val not in inverse:
        #    inverse[val] = [key]
        #else:
        #    inverse[val].append(key)
    return inverse

#print(invert_dict2(h))

liste = (10, 17, 12, 13, 11)

def has_duplicates(h):
    ref = dict()
    for n in h:
        if n in ref:
            return True
        ref[n] = True
        print(ref)
    return False

#print(has_duplicates(liste))

newlist = ('pupu', 'yuyu', 'upup')
print(newlist)
print(ord(''))

def rotate_pairs():
    for line in fin:
        
    result = dict()
    for line in fin:
        
















