#Disclaimer: this is not a reference to a specific event occuring with two towers

#creates two towers

from karel.stanfordkarel import *

#defines turn_right()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#method one
#tower one
move()
turn_left()
for i in range(3):
    put_ball()
    move()
#transition
turn_right()
move()
move()
turn_right()
move()
#tower two
put_ball()
move()
put_ball()
move()
put_ball()
turn_left()
turn_left()
for i in range(3):
    move()
turn_right()

#method two
#defines making a row
def make_row():
    for i in range(2):
        move()
        put_ball()
        move()
#first row
make_row()
turn_left()
move()
turn_left()
#second row
make_row()
turn_right()
move()
turn_right()
#third row
make_row()
turn_left()
move()
turn_left()
move()
turn_left()
turn_left()
