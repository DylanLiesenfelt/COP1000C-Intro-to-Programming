import random
import time

def diceRoll():
    return random.randint(1,6)
    
def menuNav():
    print("\n 1. See Rules.\n", "2. Play Vingt-et-un.\n", "3. Exit Program.\n")
    menu = input('Please ENTER option 1, 2, or 3: ')
    return int(menu)

def menu1():
    print('\nVingt-et-un is a dice game (known as Blackjack in the USA), where a player competes against the computer (house).\n',
        'The goal of the game is to score 21 points, or as near as possible without going over.',
        'The two players take turns throwing two dies as many times as desired and adding up the numbers thrown on each round.\n',
        '\nA player who totals over 21 is bust and loses the game.\n',
        'The player whose total is nearest 21, after each player has had a turn, wins the game.\n',
        'In the case of an equality high total, the game is tied.\n',
        '\nThe game is over at the end of a round when:\n',
        'One or both players are bust.\n',
        'Both players choose to stay.\n',
        '\nOnce a player totals 14 or more, one of the dies is discarder for the consecutive turns.\n',
        'The house must throw the dice until the total is 17 or higher. At 17 or higher, the house must stay.')

def displayScore(house, name, player):
    print(f'\nHouse: {house}  ||  {name}: {player}')
    print('-' * 25)

def houseTurn(houseScore):
    if houseScore >= 17:
        print('House Stays')
        return 0
    else:
        if houseScore > 14:
            roll1 = diceRoll()
            print(f'House Roll: {roll1}')
            return roll1
        else:
            roll1 = diceRoll()
            roll2 = diceRoll()
            print(f'House Roll: {roll1} & {roll2}')
            roll = roll1 + roll2
            return roll

def playerTurn(playerChoice, playerName, playerScore):
    if playerChoice == 'h' or playerChoice == 'H':
        if playerScore > 14:
            roll1 = diceRoll()
            print('-' * 25)
            print(f'\n{playerName} Roll: {roll1}')
            return roll1
        else:
            roll1 = diceRoll()
            roll2 = diceRoll()
            print('-' * 25)
            print(f'\n{playerName} Roll: {roll1} & {roll2}')
            roll = roll1 + roll2
            return roll
    if playerChoice == 's' or playerChoice == 'S':
        print(f'{playerName} Stays')
        return 0

def gameOver(playerScore, playerName, houseScore):
    if playerScore >= 21 or houseScore >= 21:
        if playerScore == 21 and houseScore != 21:
            print(f'{playerName} Wins: {playerScore}')
        elif playerScore != 21 and houseScore == 21:
            print(f'House Wins: {houseScore}')
        elif playerScore > 21 and houseScore <= 21:
            print(f'{playerName} Bust :( {playerScore}')
        elif playerScore <= 21 and houseScore > 21:
            print(f'House Bust {houseScore}')
        elif playerScore == 21 and houseScore == 21:
            print(f'Both {playerName} and House have 21, Draw.')





def menu2(playerName):
    houseScore = 0
    playerScore = 0
    print('\nGame Start')
    displayScore(houseScore, playerName, playerScore)
    
    while playerScore <= 21 and houseScore <= 21:
            
        playerChoice = input('ENTER h to HIT, or s to STAY:')
        while playerChoice not in ['h','H','s','S']:

            print('ERROR: You did not ENTER h or s.')
            print(playerChoice)
            playerChoice = input('ENTER h to HIT, or s to STAY:', '\n')

        else: 
            playerResult = playerTurn(playerChoice, playerName, playerScore)
            houseResult = houseTurn(houseScore)
            playerScore += playerResult
            houseScore += houseResult
            displayScore(houseScore, playerName, playerScore)
    else:
        gameOver(playerScore, playerName, houseScore)
        playAgain = input('Would you like to play again (y/n): ')
        return playAgain


def main():
    try:
        playAgain = 'y'

        print('Welcome to Vingt-en-un!')
        playerName = input('\nPlease ENTER your Name: ')

        while playAgain == 'y' or playAgain == "Y":

            menu = menuNav()
            while menu not in [1, 2, 3]:
                print('ERROR: You did not enter a number 1-3')
                menu = menuNav()

            else:
                if menu == 1:
                    menu1()
                if menu == 2:
                    playAgain = menu2(playerName)
                if menu == 3:
                    playAgain = ''     
            
        else:
            print(f'\nThanks for playing {playerName}!')
            time.sleep(1)
            print("Good Bye.")
            time.sleep(2)

    except Exception as error:
            print(f'\nERROR: {error}')
            print('Restarting Program')
            time.sleep(2)
            main()

main()