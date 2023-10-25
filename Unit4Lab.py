#weight.py
#Dylan Liesenfelt

def main(): #defines this as the main function of the program
    #Display menu options
    print("1. Display “10 ways to cut 500 calories” guideline.")
    print("2. Generate next semester expected weight table.")
    print("3. Quit")

    choice = int(input('\nPlease select option 1, 2, or 3 by entering the corresponding number: ')) #User input, priming read
    while choice > 3 or choice < 1: #Input Validation Loop, user must pick 1, 2, or 3, else loop will continue to itterate.
        print('ERROR: Invalid Input, Please Try Again.')
        choice = int(input('Please select option 1, 2, or 3 by entering the corresponding number: '))

    else: #If user input passes validation, decides whichs menu branch to continue 
        while choice == 1 or choice == 2:

            while choice == 1: #If User chooses 1
                #Displays tips
                print('\nTry these 10 ways to cut 500 calories every day.\n')
                print('* Swap your snack.')
                print('* Cut one high-calorie treat.')
                print('* DO NOT drink your calories.')
                print('* Skip seconds.')
                print('* Make low calorie substitutions.')
                print('* Ask for a doggie bag.')
                print('* Just say “no” to fried food.')
                print('* Build a thinner pizza.')
                print('* Use a smaller plate.')
                print('* Avoid alcohol.\n')
                print('Source: US National Library of Medicine\n')

                choice = int(input('Please select option 1, 2, or 3 by entering the corresponding number: ')) #User input, priming read
                while choice > 3 or choice < 1: #Input Validation Loop, user must pick 1, 2, or 3, else loop will continue to itterate.
                    print('ERROR: Invalid Input, Please Try Again.')
                    choice = int(input('Please select option 1, 2, or 3 by entering the corresponding number: '))

            while choice == 2: #If User chooses 2
                print('\nThe following will display a table based off your weight.')
                print('It will show how much you could expect to loose over the next 6 months.\n')
                weight = int(input('\nPlease enter a weight in lbs greater than 100lbs;  ')) #User input, priming read

                while weight < 100: #Input validation, User must input weight value 100 or greater, else loop will not iterate
                    print('ERROR: Invalid Input, Please Try Again.')
                    weight = int(input('Please enter a weight in lbs greater than 100lbs;  '))

                else: # Prints weight table, 4lbs subtracted from weight each month(iteration)
                    print('----------------')
                    print('Month     Weight')
                    print('----------------')

                    for month in range(1,6): # makes a table displaying months(interations) and input weight -4 for each iteration
                        print(f'  {month}  ||  {weight - 4} lbs')
                        weight -=4
                        
                    choice = int(input('\nPlease select option 1, 2, or 3 by entering the corresponding number: ')) #User input, priming read
                    while choice > 3 or choice < 1: #Input Validation Loop, user must pick 1, 2, or 3, else loop will continue to itterate.
                        print('ERROR: Invalid Input, Please Try Again.')
                        choice = int(input('Please select option 1, 2, or 3 by entering the corresponding number: ')) 

        else:#If user selects 3, exits program
            print('Good Bye')       
main()