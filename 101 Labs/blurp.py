import random
import string
specials = string.punctuation

print('Would you like to check your own password or a random one? (1 or 2)')
choice = int(input('CHOICE> '))

if choice == 1:
    print('Enter a password to validate: ')
    user_pass = input('PASSWORD> ')    
    if any(specials for i in user_pass) == True:
        print('Nice')
