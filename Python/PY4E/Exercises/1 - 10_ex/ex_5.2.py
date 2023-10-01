"""

Autograder: Exercise 5.2 Loops and Iterations

5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything 
other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.

Desired Output
Invalid input
Maximum is 10
Minimum is 2

"""

largest = None
smallest = None

while True:
    n = input("Enter a number: ")
    
    if n == "done":
        break
      
    try:
        num = int(n)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except ValueError:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
