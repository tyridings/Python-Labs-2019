# Ty Ridings
# CSCI 101 - Section D
# Python Lab EC

def recursive_sum_odd(a_list, num):
    if len(a_list) == 0:
        return num
    if (a_list[0] % 2) == 1:
        num += a_list[0]
    return recursive_sum_odd(a_list[1:],num)
