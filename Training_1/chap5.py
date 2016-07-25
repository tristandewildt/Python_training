'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math
from xlwt.antlr import ifelse

minutes = 175
hours = minutes //60
#print(hours)

remainder = minutes % 60
#print(remainder)

x=3
y=3

#if not x == y:
#    print('op')
#else:
#    print('up')


def countdown(n):
    if n== 0:
        print('Blastoff')
    elif n<0:
        return
    else:
        print(n)
        countdown(n-1)
#countdown(-1)

#prompt = 'What.. is the airspeed velocity of an unlader swallow?\n'
#speed = input(prompt)
#print(speed)
#int(speed)

import time

def time_decomp(e):
    sec = 60
    min = 60
    hours = 24
    d = e //(sec*min*hours)
    print ("Number of days is: " + str(int(d)) + " days.")
    rest = e % (sec*min*hours)
    h = rest // (sec*min)
    rest = rest % (sec*min)
    m = rest // sec
    rest = rest % (sec)
    s = rest
    print ('And the time is ' + str(int(h)) +':' + str(int(m)) + ':'+ str(int(s)))

#e = time.time()
#time_decomp(e)





def check_fermat(a, b, c, n):
    r = pow(a, n) + pow(b, n)
    y = pow(c, n)
    print(n)
    if r == y:
        print('Holy smokes, Fermat was wrong!')
    elif n >= 10:
        print('No, that doesnt work.')
    else:
        print('no')
        check_fermat(a, b, c, n + 1)
        
#print('Please give a:\n')
#a =input()
#print('Please give d:\n')
#b =input()
#print('Please give c:\n')
#c =input()
#print('Please give n:\n')
#n =input()

#print(w)

#check_fermat(a, b, c, n)
      
    
   













