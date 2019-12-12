# Ty Ridings
# CSCI 102 - Section C
# Week 11 Part A

import string
import random
punct = string.punctuation

# 1 Process a word
def clean_word(string):
    str_1 = []
    final = ''
    for i in string:
        str_1.append(i)
    for i in str_1:
        if i not in punct:
            final += i
    final = final.lower()
    final = final.replace(' ','')
    return final 

# 2 Read and process file    
def read_file(filepath):
    f = ''
    final_file = []
    with open(filepath,'r') as file:
        read_file = file.read()
        new_file = read_file.split()
    for i in new_file:
        final_file.append(clean_word(i))
    return final_file

# 3 Write random file
def write_file(word_list, output_file, word_num, seed):
    random.seed(seed) 
    with open(output_file,'w') as saved_file:
        for i in range(word_num):
            saved_file.write(random.choice(word_list) + ' ')
