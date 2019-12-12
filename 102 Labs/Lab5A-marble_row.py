# Ty Ridings
# CSCI 102 - Section C
# Week 5 - Part A

i = 0
rand_string = list(input('Please enter a string of X''s and O''s: \nMARBLES> '))
position_string = []

for i in range(len(rand_string)):

    if rand_string[i] == 'O':
        position_string.append(i)
    i = i + 1

print('Well, I did all the work Captain Lazy. I found your marbles for you, they are located at',position_string)
print('Your marble indices: \nOUTPUT ',position_string)
