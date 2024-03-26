from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    move()
    pick_beepers()
    move_twice()
    pick_beepers()
    move_twice()
    pick_beepers()
    move()
   
def pick_beepers():
    for i in range(10):
        pick_beeper()

def move_twice():
    for i in range(2):
        move()
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()