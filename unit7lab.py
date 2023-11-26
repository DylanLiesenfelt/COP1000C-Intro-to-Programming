import time
#defines a fucntion to prina lin of - 40 times
def lineGoBrrr():
    print('-' * 40)
#Answer key to the quiz 
ANSWERKEY = ['A', 'C', 'A', 'B', 'B', 'D', 'D', 'A', 'C', 'A', 'B', 'C', 'D', 'D', 'B']
#defines the main function of this program
def main():
    #usewd to restart the program loop later 
    again = 'y'
    while again == 'y' or again == 'Y':
        #error handling if no error excutes the following code
        try:
            #Sets variables used later to tally answers and grade quiz
            correctCounter = 0
            incorrectCounter = 0
            studentAnswers = []
            incorrectAnswers = []
            #user input for student name and file name 
            studentName = input('Enter the name of the student: ')
            selectedFile = input('Enter answer file in .txt format: ')
            #opens file using the user input for reading
            with open(f'{selectedFile}', 'r') as file:
                #reads the answers from the file and copys them into a new list 
                answers = file.readline().strip()
                while answers != '':
                    studentAnswers.append(answers)
                    answers = file.readline().strip()
                #compares the new list of answers to the answer key, counts correct and incorrect numbers, adds incorrect answers to the list incorrect answers
                for i in range(len(ANSWERKEY)):
                    if studentAnswers[i] == ANSWERKEY[i]:
                        correctCounter += 1
                    else:
                        incorrectCounter += 1
                        incorrectAnswers.append(i +1)
                #header information using student name input
                print(f'{studentName} Quiz Results')
                #calls linegobrr functuion to make line for header formating 
                lineGoBrrr()
                #display correct, incorrect answer total along with which question was wrong
                print(f'Correct Answers: {correctCounter}')
                print(f'Incorrect Answers: {incorrectCounter} ({incorrectAnswers})\n')
                #calc student grade
                totalQuestions = correctCounter + incorrectCounter
                grade = int((correctCounter / totalQuestions) * 100)
                #if the student scores above 60% they pass 
                if grade >= 60:
                    print(f'{studentName} PASSED the quiz with a grade of {grade}%')
                else:
                    print(f'{studentName} FAILED the quiz with a grade of {grade}%')
                #more formatting
                lineGoBrrr()
                #ask if user wants to grade another quiz if the put in 'y' the loop restarts else progrm quits 
                again = input('Would you like to grade another students quiz? (y/n): ')
        #error handling shows what the error is and restarts program        
        except Exception as error:
            print(f'\nERROR: {error}')
            print('Restarting Program')
            time.sleep(2)
            main()
    #once the user no longer submits y program exits
    else:
        print('Good Bye!')
        time.sleep(2)
#calls the main function to run
main()