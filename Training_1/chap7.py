'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math
from xlwt.antlr import ifelse
from tabulate import tabulate


def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1
    return
#print_n(4,3)

def mysqrt(a, x):
    eps = 0.0001
    while True:
        y = (x + a/float(x)) / 2
        if abs(y-x) < eps:
            break
        x = y
    return y

def test_square_root():
    a = 1
    x = 5
    table = []
    while a < 8:
        diff = (mysqrt(a, x)) - (math.sqrt(a))
        tablerow = [a,mysqrt(a, x),math.sqrt(a),diff]
        table = table + [tablerow]
        a = a + 1
    return table
#print(test_square_root())
#print(tabulate(test_square_root(), headers=["a","mysqrt(a)", "math.sqrt(a)", "diff"]))
#mysqrt(9, 8)

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def estimate_pi():
    approx = (2*math.sqrt(2))/9801
    print('first: '+ str(approx))
    k=0
    while abs(approx - math.pi) > 1e-15:
        approx = approx + (math.factorial(4*k)*(1103 + 26390*k))/(pow(math.factorial(k),4)*pow(396,4*k))
        k = k + 1
        print(approx)
    return approx
    
#print(estimate_pi())    
    
    
    






