# Ty Ridings
# CSCI 101 - Section D
# Python Lab 5B

years = int(input('Input the number of years to print in the reforestation table: \nYEARS> '))
x = 2500
i = 0

print('OUTPUT\t Year\t # Acres in Forest\t % of Forest')

while i < years:
    perc = (x / 14000)*100
    print('OUTPUT\t %d\t %d\t\t\t %0.2f' % (i,x,perc))
    x = (x * 1.02)
    i = i + 1

# Extra Credit Section    
while perc < 100.00:
    if x < 14000:
        x = (x * 1.02)
        i = i + 1
    else:
        print('OUTPUT\t It will take',i,'years to restore the forest to 100% coverage')
        break
        
