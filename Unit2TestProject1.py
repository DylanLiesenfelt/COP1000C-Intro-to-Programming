userNum = float(input('Enter number of cookies:'))

origAmount = 48.0
sugar = 1.5 / origAmount
butter = 1.0 / origAmount
flour = 2.75 / origAmount

fSugar = sugar * userNum
fButter = butter * userNum
fFlour = flour * userNum

print(f'You need {fSugar} ' +
      f'cups of sugar, {fButter} ' +
      f'cups of butter, and {fFlour} ' + 
      f'cups of flour.')

input()