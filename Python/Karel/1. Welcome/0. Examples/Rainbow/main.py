"""
File: Rainbow.py
------------------------------
Karel makes a rainbow!
"""

"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work!

Note: The unit test for this worked example is currently not working. Ignore it!
"""

from karel.stanfordkarel import *

def main():
    """
   Karel paints the squares Red, Orange, Yellow, Green, 
   and Blue in order. Karel ends on an unpainted square 
   in column 6.
    """
    paint_corner('Red')
    move()
    paint_corner('Orange')
    move()
    paint_corner('Yellow')
    move()
    paint_corner('Green')
    move()
    paint_corner('Blue')
    move()


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()