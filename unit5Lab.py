#guessNumber.py
#Dylan Liesenfelt
#COP1000C

# Implement a number guessing game where a player will get up to seven chances to guess a mystery number in the range of 1 through 100.

# At the beginning of the game, the program will generate a random number in the range 1 through 100. It will then prompt the player to guess the number. If the user’s guess is:

# Higher than the random number => the program will display “Too High …”.
# Lower than the random number => the program will display “Too Low … ”.
# The same as the random number => the program will congratulate the player.
# The program allows up to seven rounds per game. The player can play as many games as they wish.

# The following functions must be included in the implementation. They will be called from main():

# getGuess(first, last)
# Prompt user for a number in the range first to last (inclusive) and return it.
# Input Validation. Make sure that the number entered is in the range [first,last]. Loop until valid.
# guessWin(number, guess)
# Compare the mystery number against the player’s guess.
# If guess > number -> display “Too High …”
# If guess < number -> display “Too Low …”
# If guess == number -> congratulate player
# Return True if the player guessed the mystery number, False otherwise.
# Note
# Define the number of rounds per game as a constant so it can easily be adjusted to make the game more or less challenging.

import random #Imports the random libary

def main(): # Defines the main function of this program

    # Functions
    def getGuess(firstNum, lastNum, chances): # Defines getGuess function, function takes user input and returns that value to the function
        print(f'\nChances left: {chances}')
        userGuess = int(input(f'Please enter a whole number {firstNum} and {lastNum}: ')) # Assigns the users input to the variable userGuess
        while userGuess < firstNum or userGuess > lastNum: #Validation Loop
            print(f'ERROR: You entered {userGuess}. \nThat is not a whole number between {firstNum} and {lastNum}.')
            userGuess = int(input(f'\nPlease enter a whole number {firstNum} and {lastNum}: '))
        else: # If users input is within the specfied range assigned to the parameters firstNum and LastNums, then userGuess is returned to the function
            return userGuess
        
    def guessWin(guess, number): # Defines the guessWin function, determines if the user input is higher, lower, or equals the value of the random number
        if guess > number: # Checks if user input is higher than the random number, Returns value of False to the function
            print('Too high, try again.')
            return False
        elif guess < number: # Checks if user input is lower than the random number, Returns value of False to the function
            print('Too low, try again.')
            return False
        else: # If users input is not higher or lower than the random number it must equal the random number. Returns the value of True to the function
            return True

    def playAgain(): # Defines playAgain function, takes user input and returns the string's value to the function 
        playAgain = input(f'To play again enter y, to exit hit ENTER: ')
        return playAgain
    
    def game(first, last, chances): # Defines the game function, plays the game using the previous functions. 
        number = random.randint(first, last) # Assigns a random integer btween the values of the parameters fist and last to the variable number
        guessWasCorrect = False # Assigns a default value of false to the variable guessWasCorrect 
        chances # Brings the value of chances parameter into the local scope of the function

        while chances > 0: # Checks if chances are greater than zero per iteration of loop
            if guessWasCorrect == False: # If guessWasCorrect still equals False loop proceeds
                    guess = getGuess(first, last, chances) # Calls the getGuess function and assigns its value to variable guess
                    guessWasCorrect = guessWin(guess, number) # Calls guessWin variable passes the value of guess as parameter along with the value of the random number, the returned bool value rewrites the value of the variable wasGuessCorrect
                    chances -= 1 # Decreases the value of chances by per iteration of the loop
                    if guessWasCorrect == True: # If during the loop guessWasCorrect bool value was updated to equal true prints congrats message and breaks out of loop. 
                        print(f'\nCongrats {number} was the answer! You win!')
                        break
        else: # If chances decrease to 0 loop ends and loss message is displayed
            print('\nYou ran out of chances :( You lose.')
    
        playStatus = playAgain() # After loop ends calls playAgain function and assigns its returned value to playStatus and returns its value to the game function 
        return playStatus       

    # Global Variables
    FIRST_NUMBER = 1 # This number will used as the first value in the range for determining the random number added as const for later change for increased or decreased difficulty
    LAST_NUMBER = 100 # Same as FIRST_NUMBER but last number in the range.
    CHANCES = 7 # This number will be used to detremine how many chances you have in the game, added as const for same reason as FIRST_NUMBER
    playStaus = 'y' # Default value of the playStaus will be used to see if user wants to play the game

    print('Welcome to my number guessing game!') 

    while playStaus == 'y' or playStaus == 'Y': # Checks if play status equals y or Y, if so loop iterates  
        playStaus = game(FIRST_NUMBER, LAST_NUMBER, CHANCES) # Calls the game function, passes global consts as parameters for the functions, when game function completes and its value is returned as the value of the playAgain function that value  will update the playStaus variable 
    else: print('Good Bye!') # If playStatus does not equal y or Y goodbye message prints and program exits 

main()