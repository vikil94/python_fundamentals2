# Define a function called negative that accepts a number as an argument and returns a boolean (true/false) indicating whether that number is negative or not.

# Try calling it multiple times, passing in different numbers each time.

def negative(num):
    if (num > 0):
        return print("Positive")
    elif (num < 0):
        return print("Negative")

negative(5)
negative(-5)
