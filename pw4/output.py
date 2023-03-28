
from input import InputOutput
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

    elif choice == 8:
        break
    
    else:
        print("Invalid choice")