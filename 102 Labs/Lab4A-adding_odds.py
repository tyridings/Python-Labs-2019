# Ty Ridings
# CSCI 102 - Section C
# Week 4 - Part A

a = int(input('Please enter a positive integer: \nNUMBER> '))
b = int(input('Please enter another positive integer > the first: \nNUMBER> '))
sum1 = 0

while a < b < 10000:
    if (a % 2) == 0:
        a = a + 1
    elif (a % 2) == 1:
        sum1 = sum1 + a
        a = a + 2
print(sum1)
