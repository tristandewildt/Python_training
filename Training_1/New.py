'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math

class MyClass(object):
    '''
    classdocs
    '''
    radius = 5
    sphere = (4/3) * math.pi * (radius**3) 
    
    #print(sphere)
    decibels = 10*math.log(sphere)
    #print(decibels)
    
    

    def print_twice(self):
        print(self)
        print(self)
    
    def cat_twice(self, x, y):
        cat = x + y
        print(cat)
        
    def __init__(self, params):
        '''
        Constructor
        '''
        
    #print_twice('Pieter')
    #cat_twice('o', '2', '1')
    
    def do_twice(self, f):
        self.f = f()
        self.f = f()
    
    def print_spam(self, s):
        self.s = print('spam')
    
    self.s(7)
        
    

        
  
        
    
    
    
    