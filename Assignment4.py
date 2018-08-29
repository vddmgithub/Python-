import re
import math
"""
Write a Regular Expression that will match a date that follows
the following standard “YYYY-MM-DD”.
"""


str="World's the day is 1926-11-23"

dateEx = re.findall(r"[\d]{4}-[\d]{1,2}-[\d]{1,2}", str)

for elem in dateEx:
    print(elem)


"""
Write a Regular Expression that will match a traditional SSN.
"""

array = ['000123333','001245565','012548785','154878880','000-23-1234','001-23-0000','001-23-1000','120-00-1200','005-64-5541']

for elem in array:
    match = re.match("^(?!000|.+0{4})(?:\d{9}|\d{3}-\d{2}-\d{4})$", elem)
    if(match):
        ssnEx = re.findall("^(?!000|.+0{4})(?:\d{9}|\d{3}-\d{2}-\d{4})$", elem)
        print("Matches : ",ssnEx)
    else:
        print("Doesn't match: ",elem)

"""
Write a Regular Expression that will match an IPv4 address
"""
pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
ipAddress = '10.10.20.30'
print("Ip Address {0} matches IPV4 standards:  {1}".format(ipAddress, (pat.match(ipAddress) != None)))

"""
Write a Regular Expression that will match an email address.
"""
line= "My mail ID: worldHappiest@gmail.com"
match = re.search(r'[\w\.-]+@[\w\.-]+', line)
print("Mail ID: {0} is it matching? {1}".format(match.group(),(match.group()!= None)))


"""
 Calculate the area of a box.
"""
class Box(object):
    def area(self):
        return self.breadth * self.length

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


b1 = Box(10, 15)
print("Area: ", b1.area())

"""
Point class 
"""
class MyPoint:
    def __init__(self, cord1, cord2):
        self.cord1 =cord1
        self.cord2 = cord2

    def distance(self, p1):
        distance = (self.cord1 - p1.cord1)**2 +(self.cord2 - p1.cord2)**2
        return math.sqrt(distance)

p1 = MyPoint(3,4)
p2 = MyPoint(4,3)
print("Distance between two points: {0}".format(p1.distance(p2)))

"""


"""
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x-value:   {0}  y-value: {1}".format(self.x,self.y)

    def __add__(self,other):
        result = Point(0,0)
        result.x = self.x+other.x
        result .y = self.y+other.y
        return result


p1 = Point(3, 4)
p2 = Point(2, 3)
print(p1+ p2)
