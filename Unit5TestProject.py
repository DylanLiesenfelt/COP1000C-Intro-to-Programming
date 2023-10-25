# Chapter 5: Auto-Graded Programming Project 1
# Unlimited tries
# Suppose you have a certain amount of money in a savings account that earns compound monthly interest, and you want to calculate the amount that you will have after a specific number of months. The formula is as follows:
# f=p*(1+i)^t
 
# f is the future value of the account after the specified time period.
# p is the present value of the account (the account's current balance).
# i is the monthly interest rate.
# t is the number of months.
# Write a program that takes the account's present value (current balance), monthly interest rate, and the number of months that the money will be left in the account as three inputs from the user. The program should pass these values to a function that returns the future value of the account, after the specified number of months. The program should print the account's future value.
# Look carefully at the following sample run of the program. In particular, notice the wording of the messages and the placement of spaces and colons. Your program's output must match this.
# Sample Run (User input shown in bold)
# Enter current bank balance:35.7
# Enter interest rate:0
# Enter the amount of time that passes:100
# 35.7

p = float(input('Enter current bank balance:'))
i = float(input('Enter interest rate:'))
t = int(input('Enter the amount of time that passes:'))

def calcInterest(p, i, t):
    f = p * ((1 + i) ** t)
    return f

print(f'{calcInterest(p, i, t)}') # For some reason test does not want to round final number