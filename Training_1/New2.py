'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math
from xlwt.antlr import ifelse

class Restaurant(object):
    '''
    classdocs
    '''
    bankrupt = False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")
  
#    def __init__(self, params):
        
class Myclass(object): 
    x = Restaurant()
    x.bankrupt = False
    
    y = Restaurant()
    y.bankrupt = True
    
    
    Restaurant.open_branch(x)
    #print(x)
    
    
    