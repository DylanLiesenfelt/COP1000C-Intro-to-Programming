import time

def lineGoBrrr():
    print('-' * 40)

def readAnswers(data):
    line = data.readline().strip()
    return line

again = 'y'

ANSWERKEY = ['A', 'C', 'A', 'B', 'B', 'D', 'D', 'A', 'C', 'A', 'B', 'C', 'D', 'D', 'B']

while again == 'y' or again == 'Y':
    try:

        correctCounter = 0
        incorrectCounter = 0
        studentAnswers = []
        incorrectAnswers = []

        studentName = input('Enter the name of the student: ')
        selectedFile = input('Enter answer file in .txt format: ')

        with open(f'{selectedFile}', 'r') as file:

            answers = file.readline().strip()
            while answers != '':
                studentAnswers.append(answers)
                answers = file.readline().strip()

            for i in range(len(ANSWERKEY)):
                if studentAnswers[i] == ANSWERKEY[i]:
                    correctCounter += 1
                else:
                    incorrectCounter += 1
                    incorrectAnswers.append(studentAnswers[i])

            print(f'{studentName} Quiz Results')
   
            lineGoBrrr()
            print(f'Correct Answers: {correctCounter}')
            print(f'Incorrect Answers: {incorrectCounter} ({incorrectAnswers})\n')

            totalQuestions = correctCounter + incorrectCounter
            grade = int((correctCounter / totalQuestions) * 100)
            if grade >= 60:
                print(f'{studentName} PASSED the quiz with a grade of {grade}%')
            else:
                print(f'{studentName} FAILED the quiz with a grade of {grade}%')

            lineGoBrrr()

            again = input('Would you like to grade another students quiz? (y/n): ')

            
    except Exception as error:
        print(f'\nERROR: {error}')
        print('Restarting Program')
        time.sleep(2)
else:
    print('Good Bye!')
    time.sleep(2)