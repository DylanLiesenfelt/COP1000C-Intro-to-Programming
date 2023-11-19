# Assume that a file containing a series of integers is named numbers.txt. 
# Write a program that calculates the average of all the numbers stored in the file and prints the average to the screen.
# Print only the average to the screen, with no formatting. The following sample run shows an example.

with open('numbers.txt', 'r') as data:

    sum = 0
    count = 0

    line = data.readline()

    while line != '':
        num = int(line)
        sum += num
        count += 1
        line = data.readline()

    avg = sum / count

    print(f'{avg}')


