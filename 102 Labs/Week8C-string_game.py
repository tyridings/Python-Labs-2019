# Ty Ridings
# CSCI 102 - Section C
# Week 8 - Part C

import random
import string

list1 = []
list2 = []
kevin = 0
stacy = 0
vowels = 'AEIOU'

print('Would you like to: \n1.) provide your own string or 2.) generate a random one? (1 or 2)')
choice = int(input('CHOICE> '))

if choice == 1:
    print('Enter a string for the game: ')
    s = input('STRING> ')
elif choice == 2:
    print("Number to initialize the random generator: ")
    my_seed = int(input('SEED> '))
    random.seed( my_seed )
    s = ''.join(random.choice(string.ascii_uppercase) for i in range(6))

for i in range(len(s)):
    if s[i] in vowels:
        for j in range(len(s) - i):
            if s[i:len(s) - j] not in list1:
                list1.append(s[i:len(s) - j])
                kevin += 1
            elif s[i:len(s) - j] in list1:
                kevin += 1
    elif s[i] not in vowels:
        for j in range(len(s) - i):
            if s[i:len(s) - j] not in list2:
                list2.append(s[i:len(s) - j])
                stacy += 1
            elif s[i:len(s) - j] in list2:
                stacy += 1

if kevin > stacy:
    print("Kevin Wins!")
    winner = "Kevin"
elif stacy > kevin:
    print("Stacy Wins!")
    winner = "Stacy"
elif stacy == kevin:
    print("It's a Tie!")
    winner = "Draw"

print("With the string", s,", Kevin's score is", kevin,"and Stacy's score is", stacy)
print('OUTPUT ', kevin)
print('OUTPUT ', stacy)
print('OUTPUT ', winner)

