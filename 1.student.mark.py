#Create dictionary for storage students, courses and marks
students = {}
courses = {}
marks = {}

#Student information
def st_info():
    studentNum = int(input("Input the numnber of students: "))
    print(f"Input info for {studentNum} students")
    for i in range(studentNum):
        st_id = str(input("Enter student id: "))
        st_name = str(input("Enter student name: "))
        st_dob = str(input("Enter dob: "))
        students[st_id] = {'name': st_name, 'dob': st_dob}

#Courses information
def co_info():
    courseNum = int(input("Input the numnber of courses: "))
    print(f"Input info for {courseNum} courses")   
    for i in range(courseNum):
        co_id = str(input("Enter course id: "))
        co_name = str(input("Enter course name: "))
        courses[co_id] = {'course name': co_name}

#Marksheet input
def marks_info():
    co_id = input("Enter course ID: ")
    if co_id not in courses:
        print("No course with such id ")
        return
    for st_id in students:
        mark = str(input(f"Enter mark for {students[st_id]['name']}:"))
        if st_id not in marks:
            marks[st_id] = {}
        marks[st_id][co_id] = mark

#Show marksheet
def show_marks():
    co_id = input("Enter course ID: ")
    if co_id not in courses:
        print("No course with such id ")
        return
    for st_id in students:
        if st_id in marks and co_id in marks[st_id]:
            print(f"{students[st_id]['name']}: {marks[st_id][co_id]}")
        else:
            print(f"{students[st_id]['name']}: N/A")

#List functions for courses and students
def list_courses():
    print(courses)
def list_students():
    print(students)

#Main function
st_info()
co_info()
while True:
    print("Options selection")
    print('''
          1. List courses"
          2. List students"
          3. Input marks for a course"
          4. Show marks of a course"
          5. Exit
          '''
         )
    choice = int(input("Enter your choice: "))
    if choice == 1:
        list_students()
    elif choice == 2:
        list_courses()
    elif choice == 3:
        marks_info()
    elif choice == 4:
        show_marks()
    elif choice == 5:
        break
    else:
        print("Wrong choice, please try again")






         

