priColor1 = input(f'Enter primary color:')
pricolor2 = input(f'Enter primary color:')

if priColor1 == 'red' and pricolor2 == 'blue':
    print(f'When you mix {priColor1} and {pricolor2}, you get purple.')

elif priColor1 == 'red' and pricolor2 == 'yellow':
    print(f'When you mix {priColor1} and {pricolor2} you get orange.')

elif priColor1 == 'blue' and pricolor2 == 'yellow':
    print(f'When you mix {priColor1} and {pricolor2}, you get green.')

elif priColor1 == 'blue' and pricolor2 == 'red':
    print(f'When you mix {priColor1} and {pricolor2}, you get purple.')

elif priColor1 == 'yellow' and pricolor2 == 'red':
    print(f'When you mix {priColor1} and {pricolor2}, you get orange.')

elif priColor1 == 'yellow' and pricolor2 == 'blue':
    print(f'When you mix {priColor1} and {pricolor2}, you get green.')

else: 
    print('You didn\'t input two primary colors.')
    
input()

