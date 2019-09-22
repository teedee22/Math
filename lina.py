import time

from helpers import getInputVector, getInputNumber


def vectorSum(vectorA, vectorB):
    """Takes input of two vectors and outputs the linear combination of those two vectors as a tuple"""
    # Do the sum, return it as a tuple
    vectorSum = (vectorA[0] + vectorB[0], vectorA[1] + vectorB[1])
    print(f"{vectorA} + {vectorB} = {vectorSum}")
    return vectorSum


def vectorScale(vector, scalar):
    """Scale a vector by a float"""
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
            vectorA = getInputVector("first")
            vectorB = getInputVector("second")
            vectorSum(vectorA, vectorB)
            time.sleep(1)
        elif choice == "2":
            vector = getInputVector("a")
            scalar = getInputNumber()
            vectorScale(vector, scalar)
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
