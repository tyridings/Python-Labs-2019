# Ty Ridings
# CSCI 102 - Section C
# Week 7 - Part A

print('What size 2D list would you like to create?')
n = int(input('N> '))
o_list = []
r1_list = []
r2_list = []
k = 1
m = n

# Original List
print('\nThe Original List is: ')
print('OUTPUT ')
for i in range(n):
    o_array = []
    for j in range(n):
        o_array.append(k)
        k += 1
    o_list.append(o_array)
    print(o_list[i])

# Reversed list using .reverse()
print('\nThe Reversed List is: ')
print('OUTPUT ')
k = 1
for i in range(n):
    o_array = []
    for j in range(n):
        o_array.append(k)
        k += 1
    o_array.reverse()
    r1_list.append(o_array)
r1_list.reverse()
for i in range(len(r1_list)):
    print(r1_list[i])

# Reversed list without using .reverse()
print('\nThe Reversed List is: ')
print('OUTPUT ')
k = n*n
for i in range(n):
    o_array = []
    for j in range(n):
        o_array.append(k)
        k -= 1
    r2_list.append(o_array)
    print(r2_list[i])


