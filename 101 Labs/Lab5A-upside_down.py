# Ty Ridings
# CSCI 101 - Section D
# Python Lab 5A  

n = int(input('Enter a the number of tests: \nNUMBER> '))
m = n - 1
i = 0 
list1 = [0] * n

while i < n:
    list1[m] = int(input('GRADE> '))
    m = m - 1
    i = i + 1

for x in range(i):
    print('OUTPUT ',list1[x])
                 
