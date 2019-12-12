# Ty Ridings
# CSCI 102 - Section C
# Week 3 part A 

operand_one = 0
operand_two = 0

sum = 0
difference = 0
product = 0
quotient = 0
remainder = 0

operand_one = float(input('Please input a real number: \nFIRST>'))
operand_two = float(input('Please input another real number: \nSECOND>'))

print('Choose one of the following operations: \n')
print('1 - addition\n')
print('2 - subtraction\n')
print('3 - multiply\n')
print('4 - divide\n')

decision = int(input('OPERATION>'))

if decision == 1:
    sum = operand_one + operand_two
    print ('The sum of the two numbers is:\nSUM', sum)
elif decision == 2:
    difference = operand_one - operand_two
    print('The difference of the two numbers is: \nDIFFERENCE', difference)
elif decision == 3:
    product = operand_one * operand_two
    print('The product of the two numbers is: \nPRODUCT', product)
elif decision == 4:
    quotient = operand_one // operand_two
    remainder = operand_one % operand_two
    print('Difference is \nQUOTIENT',quotient,'\nRemainder is \nREMAINDER', remainder)
else:
    print ('That value is not an option, goodbye')

