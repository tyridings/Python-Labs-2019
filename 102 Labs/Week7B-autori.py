# Ty Ridings
# CSCI 102 - Section C
# Week 7 - Part B

print('What are your author names')
n = input('NAMES> ')
user = list(n)
initials = []

for i in range(len(user)):
    j = i + 1
    if user[i] == user[0]:
        initials.append(user[i])
    elif user[i] == '-':
        initials.append(user[j])       
print('OUTPUT ',''.join(initials))
    
