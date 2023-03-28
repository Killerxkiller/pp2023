#Create a class for students
class Student:
    def __init__(self, id, n, dob):
        self.__sid = id
        self.__sname = n
        self.__dob = dob
    
    def getId(self):
        return self.__sid
    
    def getName(self):
        return self.__sname
    
    def getDob(self):
        return self.__dob
    
    def setSid(self, id):
        self.__sid = id
    
    def setName(self, n):
        self.__sname = n
    
    def setDob(self, dob):
        self.__dob = dob
   