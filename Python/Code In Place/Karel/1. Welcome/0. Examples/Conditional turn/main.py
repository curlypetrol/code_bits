"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """ 
    Turns left if there is a beeper present; turns right if  there are no beepers present. 
    """
    if beepers_present():
        turn_left()
    else:
        turn_right()
    
    
def turn_right():
    for i in range(3):
        turn_left()



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()