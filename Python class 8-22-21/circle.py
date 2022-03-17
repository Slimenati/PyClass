from turtle import *

#first circle
penup()
backward(200)

forward(50)
pendown()
circle(50)

#3 other circles
for i in range(3):
    penup()
    forward(100)
    pendown()
    circle(50)
