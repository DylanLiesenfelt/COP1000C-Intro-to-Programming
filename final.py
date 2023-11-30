import random
import time

def diceRoll():
    return random.randint(1,6)
    
def menuNav():
    print("\n 1. See Rules.\n", "2. Play Vingt-et-un.\n", "3. Exit Program.\n")
    menu = input('Please ENTER option 1, 2, or 3: ')
    return int(menu)

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

def displayScore(house, name, player):
    print(f'\nHouse: {house}  ||  {name}: {player}')
    print('-' * 25)


def gameOver(playerScore, playerName, houseScore, houseStay, playerStay):
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
        elif playerScore > 21 and houseScore > 21:
            print(f'House and {playerName} both bust, Draw')
    elif houseStay == True and playerStay == True:
        if playerScore > houseScore:
            print(f'{playerName} Wins {playerScore}, House Loses {houseScore}')
        elif playerScore < houseScore:
            print(f'House Wins {houseScore}, {playerName} Loses {playerScore}')


def playerTurn(playerName, playerScore):
    if playerScore >= 14:
        roll = diceRoll()
        print(f'\n     {playerName} Roll: {roll}')
        return roll
    else:
        roll1 = diceRoll()
        roll2 = diceRoll()
        print(f'\n     {playerName} Roll: {roll1} & {roll2}')
        return roll1 + roll2

def houseTurn(houseScore):
    if houseScore >= 17:
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

def menu2(playerName):
    houseScore = 0
    playerScore = 0
    print('\nGame Start')
    displayScore(houseScore, playerName, playerScore)
    
    playerStay = False
    houseStay = False

    while not (playerStay and houseStay):
        if not playerStay:
            playerChoice = input('ENTER h to HIT, or s to STAY: ').lower()
            while playerChoice != 'h' and playerChoice != 's':
                print('ERROR: you did not enter h or s.\n')
                print(playerChoice)
                playerChoice = input('ENTER h to HIT, or s to STAY: ').lower()
            else:
                if playerChoice == 'h':
                    playerResult = playerTurn(playerName, playerScore)
                    playerScore += playerResult
                    displayScore(houseScore, playerName, playerScore)
                if playerScore >= 21:
                    playerStay = True
                elif playerChoice == 's':
                    print(f'{playerName} Stays')
                    playerStay = True
        if not houseStay:
            houseResult = houseTurn(houseScore)
            houseScore += houseResult
            displayScore(houseScore, playerName, playerScore)
            if houseScore >= 21:
                houseStay = True
            elif houseScore >= 17:
                houseStay = True

    gameOver(playerScore, playerName, houseScore, playerStay, houseStay)
    playAgain = input('\nWould you like to play again (y/n): ')
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