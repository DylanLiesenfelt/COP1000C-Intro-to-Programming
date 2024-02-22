# Assume that a file named golf.txt exists in the current working directory. The file contains the names of golfers and their final scores in a tournament. The file is structured so there is a line with the golfer's name followed by their score on the next line. Here is an example of the file's contents:
# Luka
# 72
# Mateo
# 76
# Marissa
# 74
# Rohan
# 78
# Write a program that reads the golf.txt file and prints each golfer's name and score as shown in the following sample run. Notice the placement of spaces, colons, and blank lines. Your program's output must match this.
# Sample Run:
# Name:Luka
# Score:72
# Name:Mateo
# Score:76
# Name:Marissa
# Score:74
# Name:Rohan
# Score:70

with open('golf.txt', 'r') as data:
    line = data.readline().strip()

    while line != '':
        print(f'Name:{line}')
        
        line = data.readline().strip()
        print(f'Score:{line}\n')

        line = data.readline().strip()
            
            

            
            