import time


def inputRules(vector):
    """Defines rules for user entered  vectors"""
    # Check user entered vector using comma
    if "," not in vector:
        return False
    # Check user entered two things separated by comma
    elif not len(vector.split(",")) == 2:
        return False
    # Check that user entered two numbers (floats or ints)
    try:
        [float(i) for i in vector.split(",")]
    except ValueError:
        return False
    return True


def convertToFloat(vector):
    """takes a user input vector as a string in 'a, b' format and outputs a list of floats"""
    return [float(i) for i in vector.split(",")]


def vectorSum():
    """Takes input of two vectors and outputs the linear combination of those two vectors as a tuple"""
    while True:
        vectorA = input("Please provide first vector in format a,b: ")
        if inputRules(vectorA):
            vectorA = convertToFloat(vectorA)
            break
    while True:
        vectorB = input("please provide second vector in format c,d: ")
        if inputRules(vectorB):
            vectorB = convertToFloat(vectorB)
            break

    # Do the sum, return it as a tuple
    vectorSum = (vectorA[0] + vectorB[0], vectorA[1] + vectorB[1])
    print(f"{vectorA} + {vectorB} = {vectorSum}")
    return vectorSum


def vectorScale():
    """Scale a vector by a float"""
    while True:
        vector = input("Please enter a vector in the format a,b: ")
        # Check vector entered is valid
        if inputRules(vector):
            vector = convertToFloat(vector)
            break
    while True:
        scalar = input("Please enter a number by which to scale the vector: ")
        # check vector entered is a number
        try:
            float(scalar)
            scalar = float(scalar)
            break
        except ValueError:
            print("Please enter a float or int")

    scaledVector = (vector[0] * scalar, vector[1] * scalar)
    print(f"{scalar} x {vector} = {scaledVector}")
    return scaledVector


def main():
    while True:
        print("What calculation would you like to do today?")
        choice = input("0 to quit\n1 linear combination of two vectors\n2 Scale a vector\nChoose a number: ")
        if choice == "0":
            print("Thank you for using the linear algebra calculator")
            break
        if choice == "1":
            vectorSum()
            time.sleep(1)
        elif choice == "2":
            vectorScale()
            time.sleep(1)
        else:
            print("invalid choice, enter a integer corresponding to the linear algebra calculation you would like to do")


""" Python program to plot linear algebra transformations """
"""
# Input matrix here where a and b are the i hat vectors and c and d are the j hat vectors
a = 1
b = -2
c = 3
d = 0
# Input vector to transform
vector = (-1, 2)

x = vector[0] * a + vector[1] * c
y = vector[0] * b + vector[1] * d

print(str(vector[0]) + " x " + str(a) + " + " + str(vector[1]) + " x " + str(c) + " = " + str(x))
print(str(vector[0]) + " x " + str(b) + " + " + str(vector[1]) + " x " + str(d) + " = " + str(y))
"""
if __name__ == "__main__":
    main()
