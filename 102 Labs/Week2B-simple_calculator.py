# Ty Ridings
# CSCI 102 - Section C
# Week 2 - Part B

operand_one = 0.0
operand_two = 0.0

sum = 0.0
difference = 0.0
product = 0.0
quotient = 0.0
remainder = 0.0

operand_one = int(input('input a real number: \nFIRST>'))
operand_two = int(input('input another real number: \nSECOND>'))

sum = operand_one + operand_two
difference = operand_one - operand_two
product = operand_one * operand_two
quotient = operand_one / operand_two
remainder = operand_one % operand_two

print()
print('The sum of', operand_one,'and', operand_two,'is:', sum)
print('The difference of', operand_one,'and', operand_two,'is:', difference)
print('The product of', operand_one,'and', operand_two,'is:', product)
print('The quotient of', operand_one,'and', operand_two,'is:', int(quotient))
print('The remainder of', operand_one,'and', operand_two,'is:', remainder)
