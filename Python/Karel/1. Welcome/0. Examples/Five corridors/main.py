from karel.stanfordkarel import *

def main():
    """
    Traverses 5 variable length corridors and place beepers at the ends of them if there aren't already beepers there.
    """
    for i in range(4):
        explore_corridor()
        reposition()
    explore_corridor()
    
def explore_corridor():    
    move_to_wall()
    conditional_beeper()
    turn_around()
    move_to_wall()
    turn_around()

def reposition():
    turn_left()
    move()
    turn_right()
    
def move_to_wall():
    while front_is_clear():
        move()

def turn_around():
    for i in range(2):
        turn_left()

def conditional_beeper():
    if beepers_present():
        pass
    else:
        put_beeper()

def turn_right():
    for i in range(3):
        turn_left()



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
