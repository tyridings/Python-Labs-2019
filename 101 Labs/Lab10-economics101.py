# Ty Ridings
# CSCI 101 - Section D
# Python Lab 10

import csv

def get_gdp_data(fileName, year):
    with open(fileName, 'r') as f:
        gdp_read = f.readlines()
        gdp_case = []
        for i in gdp_read:
            if i[0:4] == year:
                gdp_case.append(float(i[12:-1]))
    return gdp_case

def get_unemp_data(fileName,year):
    with open(fileName,'r') as csvfile:
        unem_case = []
        unem_nums = []
        unemp_read = csv.reader(csvfile)
        for i in unemp_read:
            unem_case.append(i)
        for i in unem_case:
            if i[0] == year:
                for j in i:
                    unem_nums.append(float(j))
        unem_nums.pop(0)
    return (unem_nums)

def get_average_gdp(gdp_list):
    avg = sum(gdp_list) / len(gdp_list)
    return avg

def get_average_unemp(unemp_list):
    avg = sum(unemp_list) / len(unemp_list)
    return avg 

print('Enter the GDP file name:')
gdp = input('GDP> ')
print('Enter the unemployment file name:')
unem = input('UNEMPLOYMENT> ')
print('Enter year to examine:')
year = input('YEAR> ')

while int(year) < 1948 or int(year) > 2018:
    print('Incorrect year, try again')
    year = input('YEAR> ')

GDP = get_gdp_data(gdp,year)
UNEMP = get_unemp_data(unem,year)
GDP_AVG = get_average_gdp(GDP)
UNEMP_AVG = get_average_unemp(UNEMP)

print('\nFor %s, the average GDP is %0.2f and the average unemployment rate is %0.1f.' % (year, GDP_AVG, UNEMP_AVG))
print('OUTPUT', year)
print('OUTPUT %0.2f' % GDP_AVG)
print('OUTPUT %0.1f' % UNEMP_AVG)
