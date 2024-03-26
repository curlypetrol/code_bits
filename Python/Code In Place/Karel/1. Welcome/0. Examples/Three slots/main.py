"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Place beepers in the bottom row of a world with 3 slots.
    """
    
    while front_is_clear():
        install_beeper()
        move()
    install_beeper()

def turn_down():
    for i in range(3):
        turn_left()

def turn_up():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()
        
def install_beeper():
        turn_down()
        move()
        put_beeper()
        turn_up()
        move()
        turn_right()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()