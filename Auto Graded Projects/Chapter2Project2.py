numberOfMales = float(input('Enter number of males:'))
numberOfFemales = float(input('Enter number of females:'))
totalNumber = float(numberOfMales + numberOfFemales)

percentMale = numberOfMales / totalNumber
percentFemale = numberOfFemales / totalNumber

print(f'Percent males: {percentMale:.0%}')
print(f'Percent females: {percentFemale:.0%}')

input()