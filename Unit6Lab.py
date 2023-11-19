# gradesSummary.py
# Implement a file processing program that generates a course grades summary report based on the course, instructor, and student data stored in a file.

# The program will prompt the user for the name of the course data file and will display a report showing:

# Course number & description
# Instructor Name
# Term
# List of students registered in the course, and their corresponding grades
# Number of students that passed & failed the course
# Course passing percentage
# Average grade for the course
# The course data file is structured as follows (per line):

# Course number & description
# Instructor Name
# Term
# List of students in the course, where each student record has two fields (two lines per student)
# Student Name
# Student Grade
# The user may process as many files as they wish.

# Notes
# Use Exception Handling to catch file processing errors such as IOError, FileNotFoundError, etc.
# Average & passing percent values are displayed with a precision of 0 decimal places.
# You may use the COP1000C.txt file attached to the Unit 6 - Lab Assignment and Submission Folder for testing purposes.


import time

#defines a function to print 70 '-' on one line
def linePrint():
    print('-' * 70)
#defines a function take file object and call readline and strip()
def newLine(data):
    return data.readline().strip()
#defines the mainfunction of the program
def main():
    #this will be used later to take user input if they wish to continue using the program
    another = 'y'
    while another == 'y' or another == 'Y':
        #error handling, if no error 
        try:
            #assining value to global variables 
            passing = 0
            failing = 0
            students = 0
            gradeSum = 0

            #take user input for file name, pass that input to open file object in read mode and assign it var file
            course = input('Please ENTER The Course File: ')
            with open(f'{course}', 'r') as file:
                #header styling 
                linePrint()
                print(f'{"COURSE SUMMARY":^70}')
                linePrint()
                #reads first line of file displays it
                course = newLine(file)
                print(f'COURSE: {course}')
                #reads second and third line of the file and displays their information
                professor = newLine(file)
                term = newLine(file)
                print(f'PROFESSOR: {professor:<41}', f'TERM: {term:>}\n')
                # more header styling
                print(f'{"STUDENT:":<20}', f'{"GRADE:":^30}')
                linePrint()
                # calling more lines from the file to use for loop
                name = newLine(file)
                grade = newLine(file)
                # while there is info to be read in the file this loop will itterate
                while name != "" or grade != "":
                    #makes grade into a interger value 
                    gradeInt = int(grade)
                    #if grade is passing add 1 to passing value
                    if gradeInt >= 60:
                        passing += 1
                    #if grade is failling add 1 to failing value
                    else:
                        failing += 1 
                    #counts how many studennts besed on how many times the loop itterates
                    students += 1
                    #while loop itterates adds the value of the grade to the gradeSum var
                    gradeSum += gradeInt 
                    #display the student info
                    print(f'{name:<20}', f'{grade:^30}')
                    # call new lines for a new student loop starts new itteration
                    name = newLine(file)
                    grade = newLine(file)
                #loop has now ended display more header styling 
                print('\nSTUDENT PERFORMANCE:')
                linePrint()
                #display the value of passing and failing students as well as displaying the % of students who passed
                print(f'PASSED: {passing:<25}', f'FAILED: {failing}')
                passPercentage = (passing / students) * 100
                print(f'PASSING PERCENT: {passPercentage:.0f}%')
                #display the average grade of the class
                gradeAvg = gradeSum / students
                print(f'AVERAGE GRADE: {gradeAvg:.0f}\n')
                # takes user input to update value of var another, this will either lead to program exit or peocessing another file
                another = input('Would  you like to process another file (y/n)')
        #error handling if thier is an error, displays what the error is and calls the main function again after a 3 second countdown        
        except Exception as error:
            print(f'\nERROR: {error}')
            print('Restarting Program in')
            countdown = 3 
            while countdown > 0:
                print(countdown)
                time.sleep(1)
                countdown -= 1
            main()
    #if user did not enter a 'y' for the input then program displays goodbye and program quits after 2 seconds      
    else:
        print("Good Bye.")
        time.sleep(2)
#calls the main function to run the program               
main()