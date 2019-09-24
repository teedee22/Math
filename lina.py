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
    """list -> list Scale any vector by a float"""
    # Rounded to 10 decimal places to avoid floating point inaccuracies
    scaledVector = [round(scalar * i, 10) for i in vector]
    print(f"{scalar} x {vector} = {scaledVector}")
    return scaledVector


def vectorTransform(matrix, vector):
    """ List -> List
    Transform a vector from a matrix input: list, output: list"""
    # 4x4 matrix by vector x,y
    if len(matrix) == 4 and len(vector) == 2:
        i = round(vector[0] * matrix[0] + vector[1] * matrix[2], 10)
        j = round(vector[0] * matrix[1] + vector[1] * matrix[3], 10)
        print(f"{vector[0]} * {matrix[0]} + {vector[1]} * {matrix[2]} = {i}")
        print(f"{vector[0]} * {matrix[1]} + {vector[1]} * {matrix[3]} = {j}")
        print((i, j))
        return [i, j]

    # 9x9 matrix by vector x,y,z
    elif len(matrix) == 9 and len(vector) == 3:
        i = round(vector[0] * matrix[0] + vector[1] * matrix[3] + vector[2] * matrix[6], 10)
        j = round(vector[0] * matrix[1] + vector[1] * matrix[4] + vector[2] * matrix[7], 10)
        k = round(vector[0] * matrix[2] + vector[1] * matrix[5] + vector[2] * matrix[8], 10)
        return [i, j, k]


def matrixMultiplication(matrixA, matrixB):
    """Multiplies matrices to give the new composition input: list, output: list"""
    # 4x4 matrix
    if len(matrixA) == 4 == len(matrixB):
        ihat = vectorTransform(matrixB, [matrixA[0], matrixA[1]])
        jhat = vectorTransform(matrixB, [matrixA[2], matrixA[3]])
        return ihat + jhat
    # 9x9 matrix
    elif len(matrixA) == 9 == len(matrixB):
        ihat = vectorTransform(matrixB, [matrixA[0], matrixA[1], matrixA[2]])
        jhat = vectorTransform(matrixB, [matrixA[3], matrixA[4], matrixA[5]])
        khat = vectorTransform(matrixB, [matrixA[6], matrixA[7], matrixA[8]])
        return ihat + jhat + khat



def main():
    while True:
        print("What calculation would you like to do today?")
        choice = input("\n\
                       0 to quit\n\
                       1 linear combination of two vectors\n\
                       2 Scale a vector\n\
                       3 Transform a 2x2 vector\n\
                       4 Transform a 3x3 vector\n\
                       5 Multiply two 2x2 matrices\n\
                       6 Multiply two 3x3 matrices\n\
                       Choose a number: ")
        if choice == "0":
            print("Thank you for using the linear algebra calculator")
            break
        if choice == "1":
            vectorA = getInputVector("first vector", "a,b", 2)
            vectorB = getInputVector("second vector", "a,b", 2)
            vectorSum(vectorA, vectorB)
            time.sleep(1)
        elif choice == "2":
            vector = getInputVector("a vector", "a,b", 2)
            scalar = getInputNumber()
            vectorScale(vector, scalar)
            time.sleep(1)
        elif choice == "3":
            matrix = getInputVector("matrix", "a,b,c,d (where a,b are ihat and c,d are jhat)", 4)
            vector = getInputVector("a vector", "a,b", 2)
            vectorTransform(matrix, vector)
        elif choice == "4":
            matrix = getInputVector("3x3 matrix", "a,b,c,d,e,f,g,h,i", 9)
            vector = getInputVector("a 3d vector", "z,y,z", 3)
            print(vectorTransform(matrix, vector))
        elif choice == "5":
            matrixA = getInputVector("matrix of first tranformation", "a,b,c,d", 4)
            matrixB = getInputVector("matrix of second transformation", "a,b,c,d", 4)
            print(matrixMultiplication(matrixA, matrixB))
        elif choice == "6":
            matrixA = getInputVector("matrix of first transformation", "a,b,c,d,e,f,g,h,i", 9)
            matrixB = getInputVector("matrix of second transformation", "a,b,c,d,e,f,g,h,i", 9)
            print(matrixMultiplication(matrixA, matrixB))
        else:
            print(
                """invalid choice, enter a integer corresponding to the linear
                 algebra calculation you would like to do"""
            )


if __name__ == "__main__":
    main()
