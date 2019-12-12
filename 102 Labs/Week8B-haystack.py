# Ty Ridings
# CSCI 102 - Section C
# Week 8 - Part B

print('Enter a DNA string s: ')
s = input('s> ')

print('Enter a substring t: ')
t = input('t> ')

list1 = []
count = 0
pos = 0
n = 0

for i in s:
    pos = s.find(t,n)
    if pos != -1:
        n = pos + 1
        count += 1
        list1.append(n)

final_list = ' '.join(map(str, list1))

print('The total number of substrings found is',count)
print('OUTPUT ', count)
print('The locations of these substrings in s are: ',final_list)
print('OUTPUT ', final_list)
