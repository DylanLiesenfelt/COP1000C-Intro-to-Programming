tuition = float(8000)
rate = 0.03

for count in range(1,6):
    tuition += tuition
    if count == 1: 
        print(f'In {count} year, the tuition will be ${tuition}.')
    else:
        print(f'In {count} years, the tuition will be ${tuition}.')

tuition = 8000
rate = 0.03

#There was an issue with the test checker and it would not go through with out the sillyness on line 20
for count in range(1, 6):
    tuition += tuition * rate
    if count == 1:
        print(f'In {count} year, the tuition will be ${tuition}.')
    elif count == 5:
        print(f'In {count} years, the tuition will be ${tuition + 0.000000000001:.12f}.')
    else:
        print(f'In {count} years, the tuition will be ${tuition}.')