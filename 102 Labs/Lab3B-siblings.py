# Ty Ridings
# CSCI 102 - Section C
# Week 3 Part B 

inp_number = input('Input a number for the siblings to consider: \nNUMBER>')

print('\nThe siblings that will work with', inp_number,'are: \n')

if int(inp_number) % 2 == 0:
    print('OUTPUT> Jimmy will ')
    
if 100 > int(inp_number) > 10:
    print('OUTPUT> Jared will ')
    if int(inp_number[0]) + int(inp_number[1]) == 8:
        print('OUTPUT> Josephine will ')    
else:
    print('OUTPUT> Sorry, none of them can help')
