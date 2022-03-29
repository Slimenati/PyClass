#creates a pyramid of balls

from karel.stanfordkarel import *

#defines turning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#bottom most row of balls
put_ball()
move()
put_ball()
move()
put_ball()
#middle row
turn_left()
move()
put_ball()
turn_left()
move()
put_ball()
turn_right()
move()
#top row
turn_right()
move()
put_ball()
