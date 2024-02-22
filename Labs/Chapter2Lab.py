# Dylan Liesenfelt
# restaurant.py Lab2

#DEFINES THE MAIN FUNCTION OF THIS PROGRAM
def main():
    #DISPLAYS A TITLE AND INSTRUCTIONS ON HOW TO USE THE PROGRAM
    print('Restaurant Bill Calculator\n')
    print('Please type in the amounts in the appropriate space.')
    print('Press the ENTER key after typing in amount to proceed. \n')

    #DISPLAYS AN INPUT TO RECEIVE USERS COST FOR CALCULATION
    food = eval(input('Cost of Food:   $'))
    drinks = eval(input('Cost of Drinks: $'))
    #USED FOR SPACE INSTEAD OF /n SO INPUT WOULD NOT DROP DOWN A LINE
    print()

    #DISPLAYS TITLE FOR THE CALCULATOR
    print('Your Bill')
    print('--------------------')
    #VARS USED FOR THE BILL CALCULATION, ROUNDED TO 2 DECI PLACES
    meal = round(food + drinks, 2)
    tax = round(meal * 0.075, 2)
    tip = round((meal + tax) * 0.18, 2)
    total = round(meal + tax + tip, 2)
    #DISPLAYS THE COST OF THE USERS BILL
    print('Cost of Meal:  $', meal)
    print('  Tax Amount:  $', tax)
    print('  Tip Amount:  $', tip)
    print('--------------------\n')
    print('Total:  $', total, '\n')
    #STOPS THE PROGRAM FROM EXITING AFTER EXECUTING CALCULATION, SO USER CAN VIEW BILL
    input('Press ENTER to close program.')
main()