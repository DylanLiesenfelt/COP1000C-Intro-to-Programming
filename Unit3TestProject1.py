month = int(input(f'Enter month (numeric):'))
day = int(input(f'Enter day:'))
year = int(input(f'Enter two digit year:'))

if day * month == year:
    print('This date is magic!')
else:
    print('This date is not magic.')

input()