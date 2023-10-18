#weightLoss.py

#Display menu options
print("1. Display “10 ways to cut 500 calories” guideline.")
print("2. Generate next semester expected weight table.")
print("3. Quit")

choice = int(input('Please select option 1, 2, or 3 by entering the corresponding number: '))
while choice != 1 or 2 or 3: 
    print('ERROR: Incorrect input.')


if choice == 1:
    print('1')
elif choice == 2:
    print('2')
elif choice == 3:
    print('3')
