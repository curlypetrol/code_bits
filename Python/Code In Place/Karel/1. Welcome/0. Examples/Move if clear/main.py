"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Karel will move and put a beeper down if there isn't a wall; Karel will just put a beeper down if there is.
    """
    
    if front_is_clear():
        move()
        put_beeper()
    else:
        put_beeper()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()