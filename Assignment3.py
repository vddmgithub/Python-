import random
import sys
"""
Build an interactive application which should simulate a Quiz
contest. The following questions might be asked as input
"""

def selectMode():
    mode = input("Select mode from EASY, INTERMEDIATE, HARD: ")
    mode_list = ["EASY", "INTERMEDIATE", "HARD"]
    if mode.upper() not in mode_list:
        sys.exit("Expecting input from EASY/INTERMEDIATE/HARD")
    else:
        return mode


def getNumberOfQuestions():
    try:
        numberOfOperations = int(input("Please give us the number of question you want to attempt: "))
        if numberOfOperations < 0:
            raise ValueError("Entered a negative input")
        else:
            return numberOfOperations
    except ValueError:
        raise ValueError("Wrong input entered expecting an integer")


def selectOperationType():
    operationType = input("Select Operation Type from M(multiplication), A(addition), S(subtraction), D(division): ")
    list = ["M","A","S","D"]

    if operationType not in list:
        raise Exception("Invalid Operation type")

    return operationType


def performOperation(operationType):
    wrongOperationType =0
    input1 = random.randint(1,10)
    input2 = random.randint(1,10)
    if operationType=="M":
        result = int(input("Multiplication of {0} and {1}: ".format(input1, input2)))
        assert (result == input1 * input2) , "Your answer is not correct"
    elif operationType=="A":
        result = int(input("Addition of {0} and {1}: ".format(input1, input2)))
        assert (result == input1 + input2), "Your answer is not correct"
    elif operationType=="S":
        result = int(input("Subtraction of {0} and {1}: ".format(input1, input2)))
        assert (result == input1 - input2), "Your answer is not correct"
    elif operationType == "D":
        result_entered_byUser = float(
        input("Please enter result up to 3 digits rounding for Division of {0} and {1}: ".format(input1, input2)))
        result = (float)("{0:.3f}".format(input1 / input2))
        assert (result_entered_byUser == result), "Your answer is not correct"


def promptUserIfHeWishesToContinue():
    return input("Continue or exit (Continue:C, Exit: E): ")


def startProcessing(num_question):
    loop = 1
    while (loop <= num_question):
        operationType = selectOperationType()
        performOperation(operationType)
        loop += 1
    else:
        while(promptUserIfHeWishesToContinue() == "C"):
            operationType = selectOperationType()
            performOperation(operationType)
        else:
            sys.exit(0)


try:
    mode = selectMode()
    num_question = getNumberOfQuestions()
    startProcessing(num_question)
except:
    print(sys.exc_info())





"""
Write a recursive function to compute x raised to the power of n.
"""

from operator import itemgetter
def power(number, pow):
    if( number == 0):
        return 0
    elif(number == 1):
        return 1
    elif (pow ==0):
        return 1
    else:
        if (pow > 0):
            return number * power(number, pow -1)
        else:
            return (1/number) * power(number, pow + 1)

"""
Sort the list using lambda function mylist = [["john", 1, "a"],
["larry", 0, "b"]]. Sort the list by second item 1 and 0.
"""
list = [["john", 1, "a"], ["larry", 0, "b"]]
soreted_list = sorted(list, key = lambda x: (x[1], x[2]))
print(soreted_list)


"""
Sort the list using operator.itemgetter function mylist = [["john",
1, "a"], ["larry", 0, "b"]]. Sort the list by second item 1 and 0.
"""
mylist = [["john",1, "a"], ["larry", 0, "b"]]
sorted_my_list = sorted(mylist,key = itemgetter(1,0))
print(sorted_my_list)