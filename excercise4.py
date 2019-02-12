# Define a function that accepts a string as an argument and returns False if the word is less than 8 characters long (or True otherwise).

def string_length(string):
    if (len(string) < 8):
        return print("False")
    elif (len(string) > 8):
        return print("True")


string_length("Liverpool")
string_length("Hello")
