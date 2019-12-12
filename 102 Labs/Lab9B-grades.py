# Ty Ridings
# CSCI 102 - Section C
# Week 9 - Part B

import csv

list1 = []
list2 = ""
in_grades = False

print('Please enter the CSV file name with student grades:')
file = input("FILE> ")

print('Please enter the name of the student to calculate grades:')
student = input("STUDENT> ")

with open(file,'r') as csvfile:
    grades = csv.reader(csvfile)
    for row in grades:
        if row[0] == student:
            s = student
            list2 += s
            for j in row[1:]:
                list1.append(int(j))
                in_grades = True

    if in_grades:
        avg = int(sum(list1)/len(list1))
        mx = max(list1)
        mn = min(list1)
        print('The average grade for',s,'is:', avg)
        print('OUTPUT',avg)
        print('The maximum grade for',s,'is:', mx)
        print('OUTPUT',mx)
        print('The minimum grade for',s,'is:', mn)
        print('OUTPUT',mn)
        for i in list1:
            list2 += ',' + str(i)
        new = open('output.txt', 'w')
        new.write(list2)
    else:
        print('Student not found. No output file created')
        print('OUTPUT error')




