#Dylan Liesenfelt
#roulette.py

#Defines this function as the main function of the program.
def main():

    #Introdcution and explanation of how to use the program.
    print('Welcome to my Roulette color program!\n')
    print('Input a number 0 - 36 below.\nThe program will tell you the corresponding color on the roulette wheel.\n')

    #Takes user's number as an integer and asigns it to variable.
    number = int(input('Enter a number 0 - 36: '))
    
    #This sequence determines what color to asign to the user's number.
    #if number is 0 it is always green.
    if number == 0:
        color = 'green'
    #Numbers 1-10 red is odd black is even.
    elif number >= 1 and number <= 10:
        if number %  2 == 0:
            color = 'black'
        else:
            color = 'red'
    #Numbers 11-18 red is even black is odd.
    elif number >= 11 and number <= 18:
        if number %  2 == 0:
            color = 'red'
        else:
            color = 'black'
    #Numbers 19-28 red is odd black is even.
    elif number >= 19 and number <= 28:
        if number %  2 == 0:
            color = 'black'
        else:
            color = 'red'
    #Numbers 29-36 red is even black is odd.
    elif number >= 29 and number <= 36:
        if number %  2 == 0:
            color = 'red'
        else:
            color = 'black'
    #If the user's number is not 0 - 36 the following error message is displayed.
    else:
        print(f'Oh No! You entered {number}, that number isn\'t between 0 - 36.\nTry again!')
        input('\nPress the ENTER key to exit.')

    #This sequence takes the evaluated information and displays it to the user.
    if color == 'green':
        print(f'You entered {number}, that number\'s color is {color}.')
    elif color == 'black':
        print(f'You entered {number}, that number\'s color is {color}.')
    elif color == 'red':
        print(f'You entered {number}, that number\'s color is {color}.')

    #Prevents program from closing at end of function
    input('\nPress the ENTER key to exit.')
main()