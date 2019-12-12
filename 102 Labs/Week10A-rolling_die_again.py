# Ty Ridings
# CSCI 102 - Section C
# Week 10 Part A

import random

print('Input the number of rolls to make: ')
num = int(input('NUMBER> '))

def function1(num_list):
    for i in range(len(num_list)):
        print('OUTPUT',i+1,'occurred',num_list[i],'times')

def function2(num_rolls):
    rolls = [0,0,0,0,0,0]

    for i in range(num_rolls):
        roll = random.randint(1,6)
        if roll == 1:
            rolls[0] = rolls[0] +1
        elif roll == 2:
            rolls[1] = rolls[1] +1
        elif roll == 3:
            rolls[2] = rolls[2] +1
        elif roll == 4:
            rolls[3] = rolls[3] +1
        elif roll == 5:
            rolls[4] = rolls[4] +1
        elif roll == 6:
            rolls[5] = rolls[5] +1

    return rolls

print('\nYour',num,'rolls follow:')
function1(function2(num))
