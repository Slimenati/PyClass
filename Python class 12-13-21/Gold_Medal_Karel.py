#creates a winners podium with Karel ending in the gold medal position
from karel.stanfordkarel import *
#defines turn_right()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#first row
move()
put_ball()
move()
put_ball()
move()
put_ball()
#second row
turn_left()
move()
turn_left()
move()
put_ball()
#karel reaches the top
turn_right()
move()
turn_right()
