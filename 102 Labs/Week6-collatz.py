# Ty Ridings
# CSCI 102 - Section C
# Week 5 - Part C

print('Enter a positive integer to generate its Collatz Conjecture')
user_num = int(input('INPUT> '))
num = user_num
my_list = []

while num != 1:
    if num % 2 == 0:
        num = int(num/2)
        my_list.append(num)
    elif num % 2 == 1:
        num = int((3 * num) + 1)
        my_list.append(num)
        
print('\nThe Collatz Conjecture for',user_num,'is: ')
print('OUTPUT ',*my_list, sep=' ')

        
