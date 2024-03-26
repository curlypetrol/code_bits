from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should be able to 
place 20 beepers, then 24 beepers, and end facing East to 
the right of the 24 beepers.
"""

def main():
    """
   This code will make Karel showcase the current year in piles of beepers
    """
    
    put_20()
    move()
    put_24()
    move()
    
    
def put_20():
    for i in range(20):
        put_beeper()

def put_24():
    for i in range(24):
        put_beeper()

if __name__ == '__main__':
    main()