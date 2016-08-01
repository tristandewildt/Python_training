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








