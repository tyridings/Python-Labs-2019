# Ty Ridings
# CSCI 102- Section C
# Week 4 - Part C

import random
my_seed = int(input("Number to initialize the random generator: \nNUMBER>"))
random.seed( my_seed )
random_num = random.randint(1,100)

guess = int(input('Enter a number between 1 and 100: \nGUESS> '))

while guess != random_num:
    if guess > 100 or guess < 1:
        print('OUTPUT Please Enter a number between 1 and 100')
    elif guess >= (random_num + 50) or guess <= (random_num - 50):
        print('OUTPUT You''re Cold!')
    elif (random_num +25) <= guess < (random_num +50) or (random_num -25) >= guess > (random_num -50):
        print('OUTPUT You''re lukewarm!')
    elif (random_num +15) <= guess < (random_num +25) or (random_num -15) >= guess > (random_num -25):
        print('OUTPUT You''re getting warmer!!')
    elif (random_num +5) <= guess < (random_num +15) or (random_num -5) >= guess > (random_num -15):
        print('OUTPUT You''re getting HOT!')
    elif guess > (random_num +5) or guess > (random_num - 5):
        print('OUTPUT You''re so close!')
    guess = int(input('\nEnter another guess: \nGUESS> '))

if guess == random_num:
    print('\nOUTPUT CONGRATS! YOU WON!')
