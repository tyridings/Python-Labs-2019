# Ty Ridings
# CSCI 101 - Section D
# Python Lab 8

import string
import random

punct = string.punctuation + string.digits
f = ''
doi = ''
rand = []
count = 0

with open('Declaration_of_independence.txt','r') as doi_file:
    doi_read = doi_file.read().lower()
    for i in doi_read:
        if i in punct:
            f += ''
        else:
            f += i
    doi = f.split()
    print(doi[:10])

    print('Would you like to print the number of times a specific word appears OR print the number of words of a specific length? (1 or 2)')
    choice = int(input('CHOICE> '))

    if choice == 1:
        print('Enter a word:')
        word = input('WORD> ').lower()
        for i in doi:
            if i == word:
                count += 1
        print('The number of times',word,'appears in the document is:',count)
        print('OUTPUT',count)

    elif choice == 2:
        print('Enter a length:')
        length = int(input('LENGTH> '))
        for i in doi:
            if len(i) == length:
                count += 1
                rand.append(i)
        print('The number of words in the document with length',length,'is:',count)
        print('OUTPUT', count)
        if len(rand) > 0:
            rand_word = random.choice(rand)
            print('One example random word of this length is:',rand_word)
            print('OUTPUT',rand_word)
        else:
            print('No example random word of this length exists')
            print('OUTPUT error')
    else:
        print('Sorry, that''s not an optional choice')
