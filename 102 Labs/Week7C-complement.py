# Ty Ridings
# CSCI 102 - Section C
# Week 7 - Part C

print('Enter a DNA string: ')
o_dna = list(input('S> '))
n_dna = []

a = 'A'
c = 'C'
g = 'G'
t = 'T'

for i in range(len(o_dna)):
    if o_dna[i] == a:
        n_dna.append(t)
    elif o_dna[i] == c:
        n_dna.append(g)
    elif o_dna[i] == g:
        n_dna.append(c)
    elif o_dna[i] == t:
        n_dna.append(a)
n_dna.reverse()

print('The Reverse complement of the above string is: ')
print('OUTPUT> ',''.join(n_dna))
