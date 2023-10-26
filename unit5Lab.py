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


# def chancesCounter(chancesLeft, wasUserCorrect):
    #     if wasUserCorrect == False and chancesLeft > 0:
    #         chancesLeft -= 1
    #         return chancesLeft
    #     elif wasUserCorrect == False and chancesLeft == 0:
    #         return chancesLeft 
    #     else:
    #         return chancesLeft

import random

def main():

    # Functions
    
    def getGuess(firstNum, lastNum, chances):
        print(f'\nChances left: {chances}')
        userGuess = int(input(f'Please enter a whole number {firstNum} and {lastNum}: '))
        while userGuess < firstNum or userGuess > lastNum:
            print(f'ERROR: You entered {userGuess}. \nThat is not a whole number between {firstNum} and {lastNum}.')
            userGuess = int(input(f'\nPlease enter a whole number {firstNum} and {lastNum}: '))
        else:
            return userGuess
        
    def guessWin(guess, number):
        if guess > number:
            print('Too high, try again.')
            return False
        elif guess < number:
            print('Too low, try again.')
            return False
        else:
            return True

    def playAgain():
        playAgain = input(f'To play again enter y, to exit hit ENTER: ')
        return playAgain
    
    def game(first, last, chances):
        number = random.randint(first, last)
        guessWasCorrect = False
        chances

        while chances > 0 and guessWasCorrect == False:
            if guessWasCorrect == False:
                    guess = getGuess(first, last, chances)
                    guessWasCorrect = guessWin(guess, number)
                    chances -= 1
                    if guessWasCorrect == True:
                        print(f'\nCongrats {number} was the answer! You win!')
                        break
        else: 
            print('\nYou ran out of chances :( You lose.')
    
        playStatus = playAgain()
        return playStatus       

    # Global Variables
    FIRST_NUMBER = 1
    LAST_NUMBER = 100
    CHANCES = 7
    playStaus = 'y'

    print('Welcome to my number guessing game!')

    while playStaus == 'y' or playStaus == 'Y':
        playStaus = game(FIRST_NUMBER, LAST_NUMBER, CHANCES)
    else: print('Good Bye!') 

main()