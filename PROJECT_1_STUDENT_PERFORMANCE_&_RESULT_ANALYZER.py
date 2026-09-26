'''
# NOTE:- I have divided this project on to 6 phases... I will complete each phase based on the topic I learn of python, we will try to go from beginner to advannce level with this project.

---------------------------------- PHASE - 1 -------------------------------
Name
Age
Department
Math Mark
English Mark
Python Mark

Then I need to store all the data to a list.

req:
    1. first of all take input from user that how many students he/she wants 
    2. then the information of all the student 
    3. then store all the student data to the program
    4. test the program with at least 5 program.
    5. when you take students name as input then you gotta handle unnecessary leading/trailing whitespaces 
    6. marks has to be on the valid range (0 - 100)
    7. and age has to be positive

'''

# to keep all the students data first need to create a empty list
students_data = []

number_of_students = int(input("How many Students do you want to add? "))
for student_number in range(number_of_students) :
    print(f"\n ----- Student {student_number + 1} -----")

    #taking the name of each student 
    name = input("Enter Student Name: ").strip()

    #now age validation to check if it's positive or not
    while True:
        age_of_students = input("Enter Age: ").strip()

        if age_of_students.isdigit(): #checking if the given string a number or not
            age = int(age_of_students) #converting age_of_students as an int

            # now checking if age is greater than 0 or not, because age has to be positive and smaller than 0 is negative
            if age > 0 :
                break # if age is greater than 0 then no need to check because already positive
            else :
                print("Age must be greater than 0.")

        else :
            print("Please enter a valid number.")

    # taking department input
    department = input("Enter Department: ").strip()

    # validating math marks 
    while True : 
        math_number = input("Enter Math Mark (0-100): ").strip()
        if math_number.isdigit() : 
            valid_math_mark = int(math_number)

            if 0 <= valid_math_mark <= 100 : #checking if the mark is between 0 - 100 if it's already between the range then no need further checking
                break
            else : 
                print("Mark must be between 0 and 100.")
        else :
            print("Please enter a valid number.")

    # validating English marks
    while True :
        english_number = input("Enter English Mark (0-100): ").strip()
        if english_number.isdigit():
            valid_english_mark = int(english_number)

            if 0 <= valid_math_mark <= 100 : #checking if the mark is between 0 - 100 if it's already between the range then no need further checking
                break
            else : 
                print("Mark must be between 0 and 100.")

        else : 
            print("Please enter a valid number.")

    # validating python makrs
    while True : 
        python_number = input("Enter Python Mark (0-100): ").strip()

        if python_number.isdigit() : 
            valid_python_mark = int(python_number)

            if 0 <= valid_python_mark <= 100 : #checking if the mark is between 0 - 100 if it's already between the range then no need further checking
                break
            else : 
                print("Mark must be between 0 and 100.")
        else :
            print("Please enter a valid number.")



    # now store all the data to a dictionary 
    student = {
        "name" : name, 
        "age" : age, 
        "department" : department,
        "math" : valid_math_mark,
        "english" : valid_english_mark,
        "python" : valid_python_mark
    }
    students_data.append(student)

#now display all students information
print("\n ===== Student Data =====")
for student in students_data :
    print(f"\n Name     :   {student['name']}")
    print(f"\n Age      :   {student['age']}")
    print(f"\n Department      :   {student['department']}")
    print(f"\n Math      :   {student['math']}")
    print(f"\n English      :   {student['english']}")
    print(f"\n Python      :   {student['python']}")