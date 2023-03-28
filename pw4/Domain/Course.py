#Create a class for courses
class Course:
    
    def __init__(self, id, n, c):
        self.__cid = id
        self.__cname = n
        self.__credits = c
    
    def getId(self):
        return self.__cid
    
    def getName(self):
        return self.__cname
    
    def getCredits(self):
        return self.__credits