# Ty Ridings
# CSCI 102 - Section C
# Week 9 - Part A

string = ''

f = open("Caged.txt", "rt")
f2 = f.read()
for i in f2:
    if i == '&':
        string += '%'
    elif i == '%':
        string += '&'
    elif i == '/':
        string += '~'
    else:
        string += i

new = open('caged_converted.txt','w')
new.write(string)

f.close()
new.close()
