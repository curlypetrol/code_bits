from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    
    collect_beeper()
    return_to_start()

def collect_beeper():
    turn_down()
    move()
    turn_left()
    triple_move()
    pick_beeper()
    
def return_to_start():
    turn_around()
    triple_move()
    turn_up()
    move()
    turn_right()

def turn_down():
    for i in range(3):
        turn_left()
    
def turn_around():
    for i in range(2):
        turn_left()    
    
def triple_move():
    for i in range(3):
        move()
        
def turn_up():
    for i in range(3):
        turn_left()
        
def turn_right():
    for i in range(3):
        turn_left()
    
    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()