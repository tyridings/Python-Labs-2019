# Ty Ridings
# CSCI 102 - Section C
# Week 5 - Part C

dna = list(input('Enter a DNA String (length < 1000): \nDNA> '))
transcribe = []
str = ""
n = 0
A = 0
C = 0
G = 0
T = 0

for i in range(len(dna)):
    if dna[n] == 'A':
        A = A + 1
        transcribe.append('A')
    elif dna[n] == 'C':
        C = C + 1
        transcribe.append('C')
    elif dna[n] == 'G':
        G = G + 1
        transcribe.append('G')
    elif dna[n] == 'T':
        T =  T + 1
        transcribe.append('U')
    else:
        print('Sorry, that''s not valid')
        break
    n = n + 1
print('OUTPUT ', A, C, G, T)
print('OUTPUT ', str.join(transcribe))
