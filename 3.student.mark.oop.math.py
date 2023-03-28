import math
import numpy as np
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
    
#Create a class for marks
class Mark:
    
    def __init__(self, mark):
        self.__mark = mark
    
    def getMark(self):
        return self.__mark
    
#Create a class for GPA
class GPA:
    def __init__(self, gpa):
        self.__gpa = gpa

    def getGpa(self):
        return self.__gpa
    
#Create a class for i/o 
class InputOutput:
    
    def __init__(self):
        self.student = {}
        self.course = {}
        self.mark = {}
        self.gpa = {}

#Input functions  
    def AddStudents(self):
        stuNum = int(input("Enter the number of students: "))
        while stuNum <= 0:
            print('invalid value')
            stuNum = int(input("Enter the number of students: "))

        for i in range(stuNum):
            sid = str(input("Enter student identifier: "))
            sname = str(input("Enter student name: "))
            dob = str(input("Enter student dob: "))

            StudentData = Student(sid, sname, dob)
            self.student[StudentData.getId()] = {'name': StudentData.getName(), 'dob': StudentData.getDob()}

    def AddCourses(self):
        courseNum = int(input("Enter the number of courses: "))
        while courseNum <= 0:
            print('invalid value')
            courseNum = int(input("Enter the number of courses: "))

        for i in range(courseNum):
            cid = str(input("Enter course identifier: "))
            cname = str(input("Enter course name: "))
            credits = int(input("Enter course credits: "))

            CourseData = Course(cid, cname, credits)
            self.course[CourseData.getId()] = {'name': CourseData.getName(), 'credits': CourseData.getCredits()}       
    
    def AddMarks(self):
        cid = input("Enter course identifier: ")
        if cid not in self.course:
            print("No course with this identifier")
            return
        
        for sid in self.student:
            mark = float(input(f"Enter the mark for {self.student[sid]['name']}: "))
            MarkData = Mark(mark)

            if sid not in self.mark:
                self.mark[sid] = {}
            self.mark[sid][cid] = {'mark': math.floor(MarkData.getMark())}


#Output functions     
    def StudentList(self):
        for id in self.student:
            print(f"Id: {id} - Name: {self.student[id]['name']} - Dob: {self.student[id]['dob']}")
    
    def CourseList(self):
        for id in self.course:
            print(f"Id: {id} - Name: {self.course[id]['name']} - Credits: {self.course[id]['credits']}")

    def Marksheet(self):
        cid = input("Enter course identifier: ")
        if cid not in self.course:
            print("No course with this identifier")
            return
        
        for sid in self.student:
            if sid in self.mark and cid in self.mark[sid]:
                print(f"{self.student[sid]['name']}: {self.mark[sid][cid]['mark']}")

            else:
                print(f"{self.student[sid]['name']}: N/A")
   
    def GpaCalc(self):      
        for sid in self.student:
            TotalCredits = 0
            TotalMarks = 0

            for cid in self.course:
                if sid in self.mark and cid in self.mark[sid]:
                    TotalCredits += self.course[cid]['credits']
                    TotalMarks += self.mark[sid][cid]['mark'] * self.course[cid]['credits']
            
            if TotalCredits > 0:
                self.gpa[sid] = {'gpa': math.floor(((TotalMarks/TotalCredits) * 10) / 10)}

            else:
                self.gpa[sid] = {'gpa': 0}

    def GpaSheet(self):        
        data = self.gpa.items()
        result = list(data)
        GPA = np.array(result)
        GPAsort = sorted(self.gpa.items(), key = lambda x:x[1]['gpa'], reverse = True)
        print(GPAsort)
                   
   
#Main function  
test = InputOutput()
while True:
    print("Options selection")
    print("1.Add students")
    print("2.Add courses")
    print("3.Show student list")
    print("4.Show course list")
    print("5.Add mark")
    print("6.Show mark")
    print("7.Show gpa")
    print("8.Quit")

    choice = int(input("Enter a choice: "))
    if choice == 1:
        test.AddStudents()

    elif choice == 2:
        test.AddCourses()

    elif choice == 3:
        test.StudentList()

    elif choice == 4:
        test.CourseList()
    
    elif choice == 5:
        test.AddMarks()
    
    elif choice == 6:
        test.Marksheet()
    
    elif choice == 7:
        test.GpaCalc()
        test.GpaSheet()

    elif choice == 8:
        break
    
    else:
        print("Invalid choice")