'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math


import turtle

t = turtle.Turtle()
length = 100
n=60
r=100
f=90

def square(t, length):
    t.fd(length)
    t.lt(90)

def polygon(t, length, n):
    t.fd(length)
    t.lt(360/n)

def circle(t, r):
    polygon(t, (2*math.pi*r)/n, n)

def arc(t,r):
    polygon(t, (2*math.pi*r)/n, n)


def do_twice(h):
    print(h)
    for i in range(n * (f / 360)):
        arc(h, r)
turtle.mainloop()

def main(e):
    do_twice(e)
#    do_twice(e)

main(t)

#bob = turtle.Turtle()
#print(bob)
#for i in range(4):
#    bob.fd(100)
#    bob.lt(90)
#turtle.mainloop()

