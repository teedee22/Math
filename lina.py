import time

from helpers import getInputVector, getInputNumber


def vectorSum(vectorA, vectorB):
    """Takes input of two vectors and outputs the linear combination of those
     two vectors as a tuple"""
    # Do the sum, return it as a tuple
    vectorSum = (vectorA[0] + vectorB[0], vectorA[1] + vectorB[1])
    print(f"{vectorA} + {vectorB} = {vectorSum}")
    return vectorSum


def vectorScale(vector, scalar):
    """Scale a vector by a float"""
    # Rounded to 10 decimal places to avoid floating point inaccuracies
    scaledVector = (
        round(vector[0] * scalar, 10),
        round(vector[1] * scalar, 10),
    )
    print(f"{scalar} x {vector} = {scaledVector}")
    return scaledVector


def vectorTransform(ihat, jhat, vector):
    """transform a vector based from ihat/jhat matrix"""
    x = round(vector[0] * ihat[0] + vector[1] * jhat[0], 10)
    y = round(vector[0] * ihat[1] + vector[1] * jhat[1], 10)
    print(f"{vector[0]} * {ihat[0]} + {vector[1]} * {jhat[0]} = {x}")
    print(f"{vector[0]} * {ihat[1]} + {vector[1]} * {jhat[1]} = {y}")
    print((x, y))
    return (x, y)


def main():
    while True:
        print("What calculation would you like to do today?")
        choice = input("\n\
                       0 to quit\n\
                       1 linear combination of two vectors\n\
                       2 Scale a vector\n\
                       3 Transform a vector\n\
                       Choose a number: ")
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
        elif choice == "3":
            ihat = getInputVector("I-hat")
            jhat = getInputVector("J-hat")
            vector = getInputVector("a")
            vectorTransform(ihat, jhat, vector)
        else:
            print(
                """invalid choice, enter a integer corresponding to the linear
                 algebra calculation you would like to do"""
            )


if __name__ == "__main__":
    main()
