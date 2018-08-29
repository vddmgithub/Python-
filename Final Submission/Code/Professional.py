"""
Pojo that holds information of Professionals
"""

class ProfessionalDetails(object):
    def __init__(self, name, working, bestWork, image):
        self.__name = name
        self.__work = working
        self.__bestWork = bestWork
        self.__image_link= image

    def getName(self):
        return self.__name

    def getProfession(self):
        return self.__work

    def getBestWork(self):
        return self.__bestWork

    def getImage(self):
        return self.__image_link

