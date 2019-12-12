# Ty Ridings
# CSCI 102 - Section C
# Week 4 - Part B

ans_1 = 0
ans_b = 0
num_tasks = 0

lots_to_do = 7
not_much_to_do = 4
task = input('Enter a task that needs done this week, or enter DONE to quit: \nTASK> ')

while task != 'DONE':
    num_tasks = num_tasks + 1
    task = input('TASK> ')

if task == 'DONE':
    if num_tasks < not_much_to_do:
        ans_1 = 'You don''t have much to do, enjoy a break!'
        ans_2 = 'FREE'
    elif not_much_to_do <= num_tasks < lots_to_do:
        ans_1 = 'You are moderately busy.'
        ans_2 = 'MODERATE'
    elif num_tasks >= lots_to_do:
        ans_1 = 'You have alot to do! Better get to work!'
        ans_2 = 'BUSY'

print('\nYou have',num_tasks,'tasks to do.', ans_1)
print('OUTPUT',num_tasks)
print('OUTPUT',ans_2)
