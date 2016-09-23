'''
Created on 22 sept. 2016

@author: Tristan
'''
#from cmath import pi
import math
import copy

"""
Time
"""

class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

time = Time()
time.hour = 9
time.minute = 59
time.second = 30

def print_time(time):
    print('%2.d' % time.hour + ":" + '%2.d' % time.minute+ ":" + '%2.d' % time.second)

#print_time(time)

"""
Pure Functions
A function is called pure if it does not modify any of the objects to it as arguments and it has no effect, like displaying a value or getting user input, other than returning a value

"""

start=Time()
start.hour=5
start.minute=10
start.second=33

duration=Time()
duration.hour=5
duration.minute=56
duration.second=3

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    if sum.second > 60:
        sum.second -= 60
        sum.minute += 1
        
    if sum.minute > 60:
        sum.minute -= 60
        sum.hour += 1
    
    return sum

final=add_time(start, duration)

#print_time(final)

"""
Modifiers
Functions that modifies the object it gets as parameters are called modifiers
"""

def increment(time, seconds):
    
    
    
    
    a = seconds//3600
    time.hour += a
    seconds=seconds - a * 3600
    
    b = seconds//60
    time.minute += b
    seconds=seconds - b * 3600
    
    time.seconds= seconds 
    return time

seconds= 300
print_time(time)
print_time(increment(time, seconds))


#print(seconds//3600)

































