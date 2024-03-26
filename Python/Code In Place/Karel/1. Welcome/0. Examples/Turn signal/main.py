"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """ If Karel is facing a wall, put a beeper, turn left and move forward."""
    
    if front_is_clear():
        pass
    else:
        put_beeper()
        turn_left()
        move()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()