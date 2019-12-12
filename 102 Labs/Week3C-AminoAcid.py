# Ty Ridings
# CSCI 102 - Section C
# Week 3 - Part C

C = int(input('Input the chemical elements of the amino acid:\nCARBON>'))
H = int(input('HYDROGEN>'))
N = int(input('NITROGEN>'))
O = int(input('OXYGEN>'))
S = int(input('SULFUR>'))

if C == 3:
    if S == 0:
        print('The amino acid for C_',C,'H_',H,'N_',N,'O_',O,'S_',S,' is Alanine')
        print('OUTPUT> C_',C,'H_',H,'N_',N,'O_',O,'S_',S,'\nOUTPUT> Alanine')
    elif S == 1:
        print('The amino acid for C_',C,'H_',H,'N_',N,'O_',O,'S_',S,' is Cysteine')
        print('OUTPUT> C_',C,'H_',H,'N_',N,'O_',O,'S_',S,'\nOUTPUT> Cysteine')  
elif C == 4:
    print('The amino acid for C_',C,'H_',H,'N_',N,'O_',O,'S_',S,' is Asparagine')
    print('OUTPUT> C_',C,'H_',H,'N_',N,'O_',O,'S_',S,'\nOUTPUT> Asparagine')
elif C == 5:
    print('The amino acid for C_',C,'H_',H,'N_',N,'O_',O,'S_',S,' is Glutamine')
    print('OUTPUT> C_',C,'H_',H,'N_',N,'O_',O,'S_',S,'\nOUTPUT> Glutamine')
elif C == 6:
    if H == 14:
        print('The amino acid for C_',C,'H_',H,'N_',N,'O_',O,'S_',S,' is Arginine')
        print('OUTPUT> C_',C,'H_',H,'N_',N,'O_',O,'S_',S,'\nOUTPUT> Arganine')
    elif H == 9:
        print('The amino acid for C_',C,'H_',H,'N_',N,'O_',O,'S_',S,' is Histidine')
        print('OUTPUT> C_',C,'H_',H,'N_',N,'O_',O,'S_',S,'\nOUTPUT> Histidine')
else:
    print('sorry, that one isn''t one the list we have')
