#Dylan Liesenfelt
#VingEtUn.py
#COP1000C

import random
import time

# Function to gererate number associated with dice roll
def diceRoll():
    return random.randint(1,6)

# Function to handle menu navigation     
def menuNav():
    print("\n 1. See Rules.\n", "2. Play Vingt-et-un.\n", "3. Exit Program.\n")
    menu = input('Please ENTER option 1, 2, or 3: ')
    return int(menu)

# Fuction to print rules of game
def menu1():
    print('\n Vingt-et-un is a dice game (known as Blackjack in the USA), where a player competes against the computer (house).\n',
        'The goal of the game is to score 21 points, or as near as possible without going over.\n',
        'The two players take turns throwing two dies as many times as desired and adding up the numbers thrown on each round.\n',
        '\n A player who totals over 21 is bust and loses the game.\n',
        'The player whose total is nearest 21, after each player has had a turn, wins the game.\n',
        'In the case of an equality high total, the game is tied.\n',
        '\n The game is over at the end of a round when:\n',
        'One or both players are bust.\n',
        'Both players choose to stay.\n',
        '\n Once a player totals 14 or more, one of the dies is discarder for the consecutive turns.\n',
        'The house must throw the dice until the total is 17 or higher. At 17 or higher, the house must stay.')

# Function that displays current score when called
def displayScore(house, name, player):
    print(f'\nHouse: {house}  ||  {name}: {player}')
    print('-' * 25)

# Function to handle game over scenarios
def gameOver(playerScore, playerName, houseScore, houseStay, playerStay):
    # Branch of if player or house has 21 or over
    if playerScore >= 21 or houseScore >= 21:
        if playerScore == 21 and houseScore != 21: # Player has 21 win condition
            print(f'{playerName} Wins: {playerScore}')
        elif playerScore != 21 and houseScore == 21: # House has 21 win condition
            print(f'House Wins: {houseScore}')
        elif playerScore > 21 and houseScore <= 21: # Player bust
            print(f'{playerName} Bust :( {playerScore}')
        elif playerScore <= 21 and houseScore > 21: # Dealer bust 
            print(f'House Bust {houseScore}')
        elif playerScore == 21 and houseScore == 21: # Both have 21, draw condtion
            print(f'Both {playerName} and House have 21, Draw.')
        elif playerScore > 21 and houseScore > 21: # Both bust, draw condition
            print(f'House and {playerName} both bust, Draw')
    elif houseStay == True and playerStay == True: #Branch where both have stayed
        if playerScore > houseScore: # Player has higher score win condition
            print(f'{playerName} Wins {playerScore}, House Loses {houseScore}')
        elif playerScore < houseScore: # House has higher score win condition
            print(f'House Wins {houseScore}, {playerName} Loses {playerScore}')

# Function to handle players turn
def playerTurn(playerName, playerScore):
    if playerScore >= 14: # if player score is 14 or more only roll one die, return the value of the roll to the function
        roll = diceRoll()
        print(f'\n     {playerName} Roll: {roll}')
        return roll 
    else: # if player score less than 14 roll two die, return the value of the roll to the function
        roll1 = diceRoll()
        roll2 = diceRoll()
        print(f'\n     {playerName} Roll: {roll1} & {roll2}')
        return roll1 + roll2

# Function to handle house turn, mostly same as players's, one exception
def houseTurn(houseScore):
    if houseScore >= 17: # house must stay at a score of 17 or more, rest is same
        print('House Stays')
        return 0
    elif houseScore >= 14:
        roll = diceRoll()
        print(f'\n     House Roll: {roll}')
        return roll
    else:
        roll1 = diceRoll()
        roll2 = diceRoll()
        print(f'\n     House Roll: {roll1} & {roll2}')
        return roll1 + roll2

# Function handles playing the actual game
def menu2(playerName):
    # Sets vars for score
    houseScore = 0
    playerScore = 0
    # Menu interface
    print('\nGame Start')
    displayScore(houseScore, playerName, playerScore)
    # Sets vars for stay condition
    playerStay = False
    houseStay = False
    # Checks condtion of stay for player and house, if not stay loop itterates
    while not (playerStay and houseStay):
        if not playerStay:
            # Display interface for user to hit or stay
            playerChoice = input('ENTER h to HIT, or s to STAY: ').lower()
            # Input validation
            while playerChoice != 'h' and playerChoice != 's':
                print('ERROR: you did not enter h or s.\n')
                print(playerChoice)
                playerChoice = input('ENTER h to HIT, or s to STAY: ').lower()
            else: # Executes players turn if hit, updates player score
                if playerChoice == 'h':
                    playerResult = playerTurn(playerName, playerScore)
                    playerScore += playerResult
                    displayScore(houseScore, playerName, playerScore)
                if playerScore >= 21: # if player 21 or bust updates stay condition to true 
                    playerStay = True
                elif playerChoice == 's': # if user inputs stay updates stay condition to true
                    print(f'{playerName} Stays')
                    playerStay = True
        if not houseStay:
            #excutes house turn if hitting, updates house score accordingly, same as player hit state, except for the 17 rule again
            houseResult = houseTurn(houseScore)
            houseScore += houseResult
            displayScore(houseScore, playerName, playerScore)
            if houseScore >= 21:
                houseStay = True
            elif houseScore >= 17:
                houseStay = True
    # Calls game over function, takes user input to play again and returns value to the function
    gameOver(playerScore, playerName, houseScore, playerStay, houseStay)
    playAgain = input('\nWould you like to play again (y/n): ').lower()
    return playAgain

# Defines the main function of this program
def main():
    # Error handling, no error execute
    try:
        # Sets var to handle play again state
        playAgain = 'y'
        # Display welcome ask for user name input
        print('Welcome to Vingt-en-un!')
        playerName = input('\nPlease ENTER your Name: ')
        # Checks play state if play good excute
        while playAgain == 'y':
            # Calls menuNav function, with input validation
            menu = menuNav()
            while menu not in [1, 2, 3]:
                print('ERROR: You did not enter a number 1-3')
                menu = menuNav()
            # Takes the returned value from menuNav to determine wich branch to go down
            else:
                if menu == 1: # display rules
                    menu1()
                if menu == 2: # play the game
                    playAgain = menu2(playerName)
                if menu == 3: # quits game
                    playAgain = ''     
        # play state no longer is set to y game quits, displays good bye message   
        else:
            print(f'\nThanks for playing {playerName}!')
            time.sleep(1)
            print("Good Bye.")
            time.sleep(2)
    # Error handling, displays the error, restarts the program by calling main again
    except Exception as error:
            print(f'\nERROR: {error}')
            print('Restarting Program')
            time.sleep(2)
            main()
#calls the main function initiates program
main() 