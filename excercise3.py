# Define a function called is_even that accepts a number as an argument and returns a boolean (true/false) indicating whether that number is even or not (HINT: use the % operator).

# Try calling it with different numbers.

def is_even(num):
    if (num % 2 == 0):
        return print("This number is even")
    elif (num % 2 == 1):
        return print("This number is odd")

is_even(5)
is_even(4)
