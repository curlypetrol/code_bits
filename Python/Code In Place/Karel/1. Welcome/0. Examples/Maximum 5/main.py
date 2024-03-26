"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Karel should place 5 beepers in the bottommost row of the world if the world is more than 5 columns wide.
    If the world is less than 5 columns wide, Karel should fill the bottommmost row with beepers and not walk through any walls.
    """
    
    put_beeper()
    for i in range(4):
        if front_is_clear():
            move()
            put_beeper()
            
        


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()