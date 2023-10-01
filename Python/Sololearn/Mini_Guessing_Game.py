"""
Mini Guessing Game 1.0

Guess the number between 1 to 100, you have 10 chances and 
you get hints if your guess is higher or lower than the target...
Should be easy enough, right?

By curlypetrol, July 2023

"""

import random

num = random.randint(1, 100)
lives = 1

num_high = 'Number is higher'
num_low = 'Number is lower'

while lives <= 10: 
    print(f"Welcome to 'Guess the Number Game'! You have {11 - lives} out of 10 chances remaining...")
    try:
        guess = int(input('Enter your guess from 1 to 100:'))

        if guess == num:
            print(f'Your guess: {guess} was right! Congrats!')
            break
        elif num > guess:
            print(num_high)
        elif num < guess:
            print(num_low)
        else:
            print("Please give a number between 1 and 100")
        lives += 1

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if lives > 10:
    print(f"Sorry, you used all your chances. The correct number was {num}.")

print("Thank you for playing")