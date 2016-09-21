'''
Created on 17 apr. 2016

@author: Tristan
'''
#from cmath import pi
import math
import copy
import turtle


class Point:
    """Represents a point in 2-D space."""

blank = Point()
blank.x = 9
blank.y = 10

black = Point()
black.x = 7
black.y = 2

#print(blank.y)

# Here Point is an object, blank is a variable and both y and z are attributes. Each attribute refers to a floating-point number.

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

#print_point(blank)
    

def distance_between_points(a,b):
    distance = math.sqrt((b.x-a.x)**2 + (b.y-a.y)**2)
    return distance

#print(distance_between_points(blank, black))


class Rectangle:
    """Represents a rectangle
    attributes: width, height, corner.
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
    p = Point()
    p.x = (rect.width + rect.corner.x) /2
    p.y = (rect.height + rect.corner.y) /2
    return p

center = find_center(box)
#print_point(center)

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    
move_rectangle(box, 100, 200)
center = find_center(box)
#print_point(center)

"""
Copying
"""
p1=Point()
p1.x=1
p1.y=2

p2 = copy.copy(p1)
#print_point(p2)

# So p2 has now the same coordinates as p1, but is not the same point

# When you copy, you're goal is not to to create new object, but have the same values as the one copied. A good copy return false for box2 = box
# shallow copy: e.g. when you perform box2=copy.copy(box), it copies the objects and the attributes, but not the embedded objects.
# In most cases, this is not what you want.
# so you may use 'deepcopy', which also copies objects within objects.

box2=copy.copy(box)
#print(box2 is box, box2.corner is box.corner)

box3=copy.deepcopy(box) 
#print(box3 is box, box3.corner is box.corner)


"""
Exo 15.1
"""

class Circle:
    """ This is a class of a circle"""


Circ = Circle()
center =  Point()
center.x=150
center.y=100
radius = 75
Circ.center = center
Circ.radius = radius

def point_in_circle(cercle,dot):
    return distance_between_points(dot,cercle.center) <= cercle.radius
    
onepoint = Point()
onepoint.x = 90
onepoint.y = 90

#print(point_in_circle(Circ,onepoint))


rect=Rectangle()
rect.corner = Point()
rect.corner.x = 100
rect.corner.y = 250
rect.width=300
rect.length=100


"""
Exo 15.2
"""

t = turtle.Turtle()

def draw_rect(turtle,rect):
    t.pu()
    turtle.goto(rect.corner.x,rect.corner.y)
    t.pd()
    turtle.fd(rect.width)
    turtle.rt(90)
    turtle.fd(rect.length)
    turtle.rt(90)
    turtle.fd(rect.width)
    turtle.rt(90)
    turtle.fd(rect.length)

draw_rect(t, rect)


turtle.mainloop()




