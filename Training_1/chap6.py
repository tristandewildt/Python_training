'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math
from xlwt.antlr import ifelse

def area(radius):
    a= math.pi * radius**2
    return a
#area(2)

def compare(x, y):
    if x < y:
        return -1
    if x == y:
        return 0
    if x > y:
        return 1
#e = compare(1, 2)
#print(e)


def distance(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    t = math.sqrt(dx ** 2 + dy ** 2)
    return t

def circle_area(x1, y1, x2, y2):
    #radius = distance(x1, y1, x2, y2)
    #result = area(radius)
    #return result
    return area(distance(x1, y1, x2, y2))

#print(circle_area(1, 1, 2, 2))

def is_between(x, y, z):
    return x <= y <= z

#print(is_between(1, 7, 3))

def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers')
        return None
    elif n < 0:
        print('Factorial is not define for negative integers')
        return None
    elif n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

#print(factorial (5.02))


def ack(m,n):
    if m == 0:
        ans = n + 1
        return ans
    elif m>0 and n == 0:
        ans = ack(m-1,1)
        return ans
    elif m>0 and n>0:
        ans = ack(m-1, ack(m,n-1))
        return ans

#print(ack(3,6))
def remainder(a,b):
    r = a % b
    return r
    
def gcd(a,b):
    if a < b:
        c = a
        a = b
        b = c
    r = remainder(a,b)
    i = 1
    gcd = 0
    if r == 0:
        return min(a,b)
    else:
        u = gcdplus(a, r, i, gcd)
        return u
     
def gcdplus(a, r, i, gcd):   
    if i <= a and i <= r:
        y = a % i
        z = r % i
        if y == 0 and z == 0:
            gcd = i
        return gcdplus(a,r,i+1,gcd)
    else:
        return gcd#(stop)
res = gcd(6,30)
print('Greatest common divisor is: ' + str(res))
#print()
    
    








