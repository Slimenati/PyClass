from turtle import *

#sets position
speed(0)
penup()
setposition(-100, 0)
pensize(5)

#draws four triangles 
for i in range(4):
    pendown()
    color('red')
    forward(50)
    left(120)
    color('blue')
    forward(50)
    left(120)
    color('green')
    forward(50)
    left(120)
    penup()
    forward(50)
