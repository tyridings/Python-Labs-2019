the_str = input('input a string here: ')

firstNum = int(input('first starting indices integer: '))
secNum = int(input('first ending indices integer: '))
thirdNum = int(input('second starting indices integer: '))
fourthNum = int(input('second ending indices integer: '))

str1 = the_str[firstNum:secNum+1] 
str2 = the_str[thirdNum:fourthNum+1]

print (str1,'', str2)
