input = "Discover, Learning, with, Edureka"


"""
Problem 1 
Number of lowercase “a” and “o” in the following sentence.
Number of uppercase “L” and “N” in the following sentence.
"""

print("Number of a's : {0}  and  o's : {1}".format(input.count("a"), input.count("o")))
print("Number of L's : {0}  and  N's : {1}".format(input.count("L"), input.count("N")))


"""
Problem 2
Input : "www.edureka.in"
a. Remove all w’s before and after .edureka.
b. Remove all lowercase letter before and after .edureka.
c. Remove all printable characters
"""
input = "www.edureka.in"
index = input.find(".edureka.")

firstResult = input[0:3].replace("w","")+input[3:]
print("firstResult: ",firstResult)

secondResult=""
for c in input[:index]:
    if not c.islower():
        secondResult += c

secondResult += ".edureka."

for c in input[index + len(".edureka."):]:
    if not c.islower():
        secondResult += c

print("After removing all lowercase letters before and after .edureka. in the input string: "+secondResult)

#Removing all Printable characters
thirdString = ""
for c in input:
    if not c.isprintable():
        thirdString += c

print("After removing all printable charcters from www.edureka.in: ", thirdString)

"""
Problem 3 
Identify the type of numbers
"""
print("0X7AE is of type: ",type(0X7AE))
print("3+4j is of type: ", type(3+4j))
print("3.14e-2 is of type: ", type(3.14e-2))
print("-01234 is of type: ", type(-1234))


"""
Problem 4
. Write a program for String Formatting Operator % which should
include the following conversions: 
1. Character
2. Signed decimal integer
3. Octal integer
4. Hexadecimal integer (UPPERcase letters)
5. Floating point real number
6. Exponential notation (with lowercase 'e')
"""
print('ABC%c' % 'D')
print("%d" % -3)
print("%o" % 16)
print("%x" % 16)
print("%f" % 3.14)
print("%e" % 10)