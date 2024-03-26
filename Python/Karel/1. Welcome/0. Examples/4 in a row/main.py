"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """ Places 4 beepers in a row, starting with the position Karel is currently on. """
    for i in range(3):
        put_beeper()
        move()
    put_beeper()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()