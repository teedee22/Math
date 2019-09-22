

def vectorSum():
    """Takes input of two vectors and outputs their sum"""
    def inputRules(vector):
        # Check user entered vector using comma
        if ", " not in vector:
            return False
        # Check user entered two things separated by comma
        elif not len(vector.split(", ")) == 2:
            return False
        # Check that user entered two integers
        try:
            [int(i) for i in vector.split(", ")]
        except ValueError:
            return False
        return True

    while True:
        vectorA = input("Please provide first vector in format a, b")
        if inputRules(vectorA):
            break
    while True:
        vectorB = input("please provide second vector in format c, d")
        if inputRules(vectorB):
            break

    # Convert vectors to integers and store them in tuples
    vectorTuple = ([int(i) for i in vectorA.split(", ")], [int(i) for i in vectorB.split(", ")])
    vectorSum = (vectorTuple[0][0] + vectorTuple[1][0], vectorTuple[0][1] + vectorTuple[1][1])
    print(f"{vectorTuple[0]} + {vectorTuple[1]} = {vectorSum}")
    return vectorSum


while True:
    print("What calculation would you like to do today?")
    choice = input("1 for sum of two vectors\nChoose a number: ")
    if choice == "1":
        vectorSum()
    else:
        print("invalid choice, enter a integer corresponding to the linear algebra calculation you would like to do")
