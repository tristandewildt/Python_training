'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math
from xlwt.antlr import ifelse
from tabulate import tabulate
from sympy.core.numbers import NumberSymbol



cheeses = ['penuts', 'mango', 'tree']
p = 'manga' in cheeses

#for o in cheeses:
#    print (o)

numbers = [8, 4 , 5 ,7]
bignumbers = [102,410,584]

def add_all(t):
    total = 0
    for x in t:
        total += x
    return total




#for i in range(len(numbers)):
#    numbers[i]= numbers[i] * 2
#print (numbers)

#print (numbers[2:])
numbers[1:3] = [14,16]

numbers.append(52)
#print(numbers)

bignumbers.extend(numbers)
bignumbers.sort()

#print(numbers)
#numbers.pop(0)
#numbers.remove(14)
#del numbers[2]
#print(numbers)

#print(add_all(bignumbers))
#print(sum(bignumbers))#print(bignumbers)

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

#print(capitalize_all(cheeses))

s = "popper"
y = list(s)
#print(y)

n = "Live-is-good"
bar = "-"
r = n.split(bar)
#print(r)

a = [2, 3, 1]
b = a
b.sort()
#print(a)

def tail(t):
    return t[1:]

yu = [1,5,4,8,9,4,7]
#print(tail(yu))
t = [[1, 2], [3], [4, 5, 6]]
def nested_sum(t):
    total = 0
    for n in t:
        total += sum(n)
    return total

#print(nested_sum(t))
g = [1, 2, 3]
def cumsum(g):
    r = []
    du = 0
    for n in g:
        du += n
        r.append(du)
    return r
#print(cumsum(g))


t = [1,2,3,4]
def chop(t):
    del t[0]
    r = len(t) - 1
    del t[r]
    return t

#print(chop(t))

def is_sorted(t):
    n=0
    while n < len(t)-1:
        if t[n] < t[n+1]:
            
            n += 1
        else:
            return False
    return True 

def ask():
    olist = []
    print("Give me a first integer:")
    r = input()
    while r != -1:
        olist.append(r)
        print("Give me another integer, or print stop if finished:1")
        r = input()
    print(olist)
    print('Sorted?')
    return is_sorted(olist)

print(ask())






