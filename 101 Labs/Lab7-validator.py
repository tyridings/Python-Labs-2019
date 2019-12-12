# Ty Ridings
# CSCI 101 - Section D
# Python Lab 7

import random
import string

specials = string.punctuation
upper = string.ascii_uppercase
lower = string.ascii_lowercase
rand_ltr = string.ascii_letters
rand_digt = string.digits
vowels = 'aeiouAEIOU'
valid = 0
score = 0
up = 0
low = 0
list1 = []

print('Would you like to check your own password or a random one? (1 or 2)')
choice = int(input('CHOICE> '))

if choice == 1:
    print('Enter a password to validate: ')
    user_pass = input('PASSWORD> ')
    if len(user_pass) >= 8 and any(str.isdigit(i) for i in user_pass) == True:
        for i in specials:
            if i in user_pass:
                valid = 1

elif choice == 2:
    print("Number to initialize the random generator: ")
    my_seed = int(input('SEED> '))
    random.seed( my_seed )
    letters = ''.join(random.choice(rand_ltr) for i in range(8))
    numbers = ''.join(random.choice(rand_digt) for j in range(2))
    punct = ''.join(random.choice(specials) for k in range(2))
    user_pass = letters + numbers + punct
    valid = 1

if valid == 1:
    for i in user_pass:
        if i not in list1:
            list1.append(i)

    for i in list1:
        n = user_pass.count(i)
        if i in rand_ltr:
            score += n*4
            if i in vowels:
                score -= n*3
        elif i in rand_digt:
            score += n*5
        elif i in specials:
            score += n*6

    for i in list1:
        n = user_pass.count(i)
        if i in upper:
            up += n
        elif i in lower:
            low += n
    score += (up - low) * 2

    if score < 20:
        output = 'Weak+'
    elif score >= 20 and score < 40:
        output = 'Weak'
    elif score >= 40 and score < 60:
        output = 'Good'
    elif score >= 60 and score < 80:
        output = 'Strong'
    elif score >= 80:
        output = 'Strong+'

    print('Validating the password',user_pass)
    print('The password', user_pass,'is a', output,'password')
    print('OUTPUT ', output)

elif valid == 0:
    print('Validating the password', user_pass)
    print('The password', user_pass,'is an INVALID password')
    print('OUTPUT INVALID')
