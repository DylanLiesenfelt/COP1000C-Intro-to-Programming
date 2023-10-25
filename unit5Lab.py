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

import random

def main ():

    #Global Variables
    FIRST = 1 # First number in the random number's range
    LAST = 100 # Last number in the random number's range
    ROUNDS = 7 # Assigns the value to the number of rounds
    isGuessCorrect = False # Used later to determine if the guess was correct
    playAgain = 'y'
    # print(f'TEST: Answer {number}') # Test output to see number

    def getGuess(first,last): # Function to get user input for guessing the number
        guess = int(input(f'Please Enter A Number {first} - {last}: ')) # Assigns the value of the user input to guess variable
        while guess > 100 or guess < 1: # Input validation loop, checks if number is range of FIRST and LAST
            print(f'\nERROR: You Input {guess}. That Number Is Not In The Range {first} - {last}.') # Error message for if user fails input validation
            guess = int(input(f'Please Enter A Number {first} - {last}: ')) # Ask user to enter value again
        else:     
            return guess # If user input passes validation retuens the value of guess to the function
        
    def guessWin(number, guess): # Function to see if user guess matches the number
        if guess > number: # Checks if user guess is higher than number, if so tells them thier guess is higher and returns a value of false to the function
            print('\nToo High, Try Again')
            return False
        elif guess < number: # Checks if user guess is lower than number, if so tells them thier guess is lower and returns a value of false to the function
            print('\nToo Low, Try Again')
            return False
        else: # If users gues is not higher or lower it must equal the guess, congratulates the player and  returns value of true to the function
            print(f'\nCongrats You Gussed Right! {number} Was The Answer! YOU WIN!' )
            return True
        
    print('\nWelcome To My Guess The Number Game!')
    
    def game(guessCorrect, rounds):

        print(f'You Will Have {ROUNDS} Chances To Guess The Number Correctly, Else You Lose :(')
        number = random.randint(FIRST, LAST) # Assigns the value of the random number
        
        while guessCorrect == False:
            if rounds == 0:
                print('\nYou Ran Out Of Chances to Guess. You Lose :(')
                playAgain = input('Enter Y To Play Again: ')
                return playAgain
            else: 
                print(f'\nChances Left: {rounds}')
                guess = getGuess(FIRST, LAST)
                isGuessCorrect = guessWin(number, guess)
                if isGuessCorrect == False:
                    rounds -= 1
                else:
                    return isGuessCorrect
            playAgain = input('Enter Y To Play Again: ')
            return playAgain
    
    while playAgain == 'y' or playAgain == 'Y':
        game(isGuessCorrect, ROUNDS)
    else:
        print('Thanks For Playing! Good Bye')




main ()    