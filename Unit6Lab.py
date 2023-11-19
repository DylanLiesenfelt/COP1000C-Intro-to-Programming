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

def linePrint():
    print('----------------------------------------------------------------------')

def newLine(data):
    return data.readline().strip()

def main():
    
    another = 'y'
    while another == 'y' or another == 'Y':
        try:
            
            passing = 0
            failing = 0
            students = 0
            gradeSum = 0

        

            course = input('Please ENTER The Course File: ')
            with open(f'{course}') as file:
                
                linePrint()
                print(f'{"COURSE SUMMARY":^70}')
                linePrint()

                course = newLine(file)
                print(f'COURSE: {course}')

                professor = newLine(file)
                term = newLine(file)
                print(f'PROFESSOR: {professor:<41}', f'TERM: {term:>}\n')
                
                print(f'{"STUDENT:":<20}', f'{"GRADE:":^30}')
                linePrint()
                
                name = newLine(file)
                grade = newLine(file)
                while name != "" or grade != "":
                    gradeInt = int(grade)
                    if gradeInt >= 60:
                        passing += 1
                    else:
                        failing += 1 
                    students += 1
                    gradeSum += gradeInt 
                    print(f'{name:<20}', f'{grade:^30}')

                    name = newLine(file)
                    grade = newLine(file)

                print('\nSTUDENT PERFORMANCE:')
                linePrint()

                print(f'PASSED: {passing:<25}', f'FAILED: {failing}')
                passPercentage = (passing / students) * 100

                print(f'PASSING PERCENT: {passPercentage:.0f}%')
                gradeAvg = gradeSum / 0

                print(f'AVERAGE GRADE: {gradeAvg:.0f}\n')

                another = input('Would  you like to process another file (y/n)')
                
        except Exception as error:
            print(f'\nERROR: {error}')
            print('Restarting Program in')
            countdown = 3 
            while countdown > 0:
                print(countdown)
                time.sleep(1)
                countdown -= 1
            main()
           
    else:
        print("Good Bye.")
        time.sleep(2)
               
main()