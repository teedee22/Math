"""
Helper functions for linear algebra programme
"""


def inputRulesVector(vector, quantity):
    """Defines rules for user entered vectors"""
    # Check user entered vector using comma
    if "," not in vector:
        return False
    # Check user entered two things separated by comma
    elif not len(vector.split(",")) == quantity:
        return False
    # Check that user entered two numbers (floats or ints)
    try:
        [float(i) for i in vector.split(",")]
    except ValueError:
        return False
    return True


def inputRulesNumber(number):
    """Defines rules for user entered numbers e.g. integer or float"""
    try:
        float(number)
        return True
    except ValueError:
        return False


def convertToFloat(vector):
    """takes a user input vector as a string in 'a, b' format and outputs a list of floats"""
    return [float(i) for i in vector.split(",")]


def getInputVector(message, format, quantity):
    """Gets input from user, quantity is a string for first, second third etc returns a list of floats"""
    while True:
        vectorA = input(f"Please provide {message} in the format {format}: ")
        if inputRulesVector(vectorA, quantity):
            return convertToFloat(vectorA)


def getInputNumber():
    """Checks a value entered is float or integer before returning a float"""
    while True:
        scalar = input("Please enter a number by which to scale the vector: ")
        if inputRulesNumber(scalar):
            return float(scalar)
