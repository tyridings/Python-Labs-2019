# Ty Ridings
# CSCI 102 - Section C
# Week 8 - Part A

import random

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
roll = 0

print('Input the number of rolls to make: ')
num = int(input('NUMBER> '))

for i in range(num):
    roll = random.randint(1,6)
    if roll == 1:
        one += 1
    elif roll == 2:
        two += 1
    elif roll == 3:
        three += 1
    elif roll == 4:
        four += 1
    elif roll == 5:
        five += 1
    elif roll == 6:
        six += 1

print('\nYour', num,'rolls follow: ')
print('OUTPUT 1 occurred', one,'times')
print('OUTPUT 2 occurred', two,'times')
print('OUTPUT 3 occurred', three,'times')
print('OUTPUT 4 occurred', four,'times')
print('OUTPUT 5 occurred', five,'times')
print('OUTPUT 6 occurred', six,'times')
