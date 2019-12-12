# Ty Ridings
# CSCI 101 - Section D
# Python Lab 9

def Multiply(a,b,output):
    prod = a * b
    if prod == output:
        return True
    else:
        return False

def BoundsChecking(lower,upper,list_length):
    if lower >= 0 and upper > lower and upper <= list_length:
        return True
    else:
        return False

def DecimalPoints(float_num):
    input_num = str(float_num)
    inp_list = input_num.split('.')
    if len(inp_list[1]) == 3:
        return True
    else:
        return False
    
def ListSorted(some_list):
    og_list = []
    for i in some_list:
        og_list.append(i)
    some_list.sort()
    if og_list == some_list:
        return True
    else:
        return False
    
def ReversedList(list_1,list_2):
    list_1.reverse()
    if list_1 == list_2:
        return True
    else:
        return False

def NumZeros(integer,two_d_list):
    count = 0
    for i in range(len(two_d_list)):
        for j in two_d_list[i]:
            if j == 'o' or j == 'O':
                count += 1
    if integer == count:
        return True
    else:
        return False

def CheckCS(string):
    c = string.find('c')
    s = string.find('s')
    if c > -1 and s > -1:
        if c < s:
            return True
        elif c > s:
            return False
    else:
        return False
