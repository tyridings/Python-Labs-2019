# Ty Ridings
# CSCI 101 - Section D
# Python Lab 6

print('Enter the number or test intervals')
n = int(input('N> '))
print('Enter your input in the following format: N D H M ')
max_hour = 1440 # This represents the clock-hour 24 00 in minutes (24 * 60)
min_time = 0
hour = 0
minute = 0

for i in range(n):
    list1 = input('INPUT> ')
    user = list1.split()
    time = (int(user[2]) * 60) + (int(user[3]))
    if user[0] == 'F':
        time = time + int(user[1])
        if time > max_hour:
            time = time - max_hour
            hour = time // 60
            minute = time % 60
        else:
            hour = time // 60
            minute = time % 60
    elif user[0] == 'B':
        time = time - int(user[1])
        if time < min_time:
            time = time + max_hour
            hour = time // 60
            minute = time % 60
        else:
            hour = time // 60
            minute = time % 60
    print('OUTPUT ',hour,minute)
