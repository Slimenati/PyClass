"""this program will construct a pyramid shape of circles centered around the y axis with 3 at the bottom,
2 in the middle, and 1 at the top, each with a radius of 50."""
from turtle import *

#this code centers tracy at the middle bottom, then draws 3 circles
speed(0)
penup()
setposition(-100, -200)
for i in range (3):
    pendown()
    circle(50)
    penup()
    forward(100)
    
#this code centers tracy at the middle upper bottom, then draws 2 circles
setposition(-50, -100)
for i in range (2):
    pendown()
    circle(50)
    penup()
    forward(100)
    
#this code centers tracy in the middle of the coordinate plane, then draws 1 circle
setposition(0, 0)
for i in range (1):
    pendown()
    circle(50)
    penup()
    forward(100)
