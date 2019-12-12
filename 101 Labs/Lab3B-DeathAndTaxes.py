# Ty Ridings
# CSCI 101 - Section C
# Python Lab 3B

income = int(input('Please enter how much you made in dollars last year:\nINCOME>'))
status = input('Please enter your filing status:\nSTATUS>')
tax_amount = 0
tax_percent = 0

if status == 'single':
    if income <= 9325:
        tax_amount = int(income*0.95)
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by single filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))
        
    elif 9325 < income <= 37950: 
        tax_amount = int(((income - 9325)*0.15)+ (9325*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by single filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))
        
    elif 37950 < income <= 91900:
        tax_amount = int(((income - 37950)*0.25) + ((37950 - 9325)*0.15) + (9325*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by single filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))
        
    elif 91901 < income <= 191650:
        tax_amount = int(((income - 91901)*0.28) + ((91901 - 37950)*0.25) + ((37950 - 9325)*0.15) + (9325*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by single filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))
        
    elif 191650 < income <= 416700:
        tax_amount = int(((income - 191650)*0.33) + ((191650 - 91901)*0.28) + ((91901 - 37950)*0.25) + ((37950 - 9325)*0.15) + (9325*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by single filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))
        
    elif 416700 < income <= 418400:
        tax_amount = int(((income - 416700)*0.35) + ((416700 - 191650)*0.33) + ((191650 - 91901)*0.28) + ((91901 - 37950)*0.25) + ((37950 - 9325)*0.15) + (9325*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by single filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))

    elif 418400 < income:
        tax_amount = int(((income-418400)*0.396) + ((418400 - 416700)*0.35) + ((416700 - 191650)*0.33) + ((191650 - 91901)*0.28) + ((91901 - 37950)*0.25) + ((37950 - 9325)*0.15) + (9325*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by single filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))

elif status == 'joint':   
    if income < 18650:
        tax_amount = int(income*0.1)
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by joint filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))
        
    elif 18650 < income <= 75900:
        tax_amount = int(((income - 18650)*0.15) + (18650*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by joint filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))
        
    elif 75900 < income <= 153100:
        tax_amount = int(((income - 75900)*0.25) + ((75900 - 18650)*0.15) + (18650*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by joint filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))
        
    elif 153100 < income <= 233350:
        tax_amount = int(((income - 153100)*0.28) + ((153100 - 75900)*0.25) + ((75900 - 18650)*0.15) + (18650*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by joint filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))
        
    elif 233350 < income <= 416700:
        tax_amount = int(((income - 233350)*0.33) + ((233350 - 153100)*0.28) + ((153100 - 75900)*0.25) + ((75900 - 18650)*0.15) + (18650*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by joint filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))
        
    elif 416700 < income <= 470700:
        tax_amount = int(((income - 416700)*0.35) + ((416700 - 233350)*0.33) + ((233350 - 153100)*0.28) + ((153100 - 75900)*0.25) + ((75900 - 18650)*0.15) + (18650*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by joint filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))
    
    elif 470700 < income:
        tax_amount = int(((income - 470700)*0.396) + ((470700 - 416700)*0.35) + ((416700 - 233350)*0.33) + ((233350 - 153100)*0.28) + ((153100 - 75900)*0.25) + ((75900 - 18650)*0.15) + (18650*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by joint filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))

elif status == 'seperate':
     if income <= 9325 :
        tax_amount = int(income*0.1)
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by seperate filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))

     elif 37950 < income <= 76550 :
        tax_amount = int(((income - 37950)*0.25) + ((37950 - 9325)*0.15) + (9326*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by seperate filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))

     elif 76550 < income <= 116675 :
        tax_amount = int(((income - 76550)*0.28) + ((76550 - 37950)*0.25) + ((37950 - 9325)*0.15) + (9326*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by seperate filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))

     elif 116675 < income <= 208350 :
        tax_amount = int(((income - 116675)*0.33) + ((116675 - 76550)*0.28) + ((76550 - 37950)*0.25) + ((37950 - 9325)*0.15) + (9326*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by seperate filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))
        
     elif 208350 < income <= 235350 :
        tax_amount = int(((income - 208350)*0.35) + ((208350 - 116675)*0.33) + ((116675 - 76550)*0.28) + ((76550 - 37950)*0.25) + ((37950 - 9325)*0.15) + (9326*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by seperate filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))   
        
     elif 235350 < income:
        tax_amount = int(((income - 235350)*0.396) + ((235350 - 208350)*0.35) + ((208350 - 116675)*0.33) + ((116675 - 76550)*0.28) + ((76550 - 37950)*0.25) + ((37950 - 9325)*0.15) + (9326*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by seperate filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))   

elif status == 'head':
     if income < 13350:
        tax_amount = int(income*0.1)
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by head of household filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))

     elif 13350 < income <= 50800:
        tax_amount = int(((income - 13350)*0.15) + (13350*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by head of household filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))

     elif 50800 < income <= 131200:
        tax_amount = int(((income - 50800)*0.25) + ((50800 - 13350)*0.15) + (13350*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by head of household filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2)) 

     elif 131200 < income <= 212500:
        tax_amount = int(((income - 131200)*0.28) + ((131200 - 50800)*0.25) + ((50800 - 13350)*0.15) + (13350*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by head of household filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2)) 

     elif 212500 < income <= 416700:
        tax_amount = int(((income - 212500)*0.33) + ((212500 - 131200)*0.28) + ((131200 - 50800)*0.25) + ((50800 - 13350)*0.15) + (13350*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by head of household filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))  

     elif 416700 < income <= 444500:
        tax_amount = int(((income - 416700)*0.35) + ((416700 - 212500)*0.33) + ((212500 - 131200)*0.28) + ((131200 - 50800)*0.25) + ((50800 - 13350)*0.15) + (13350*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by head of household filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))  

     elif 444500 < income:
        tax_amount = int(((income - 444500)*0.396) + ((444500 - 416700)*0.35) + ((416700 - 212500)*0.33) + ((212500 - 131200)*0.28) + ((131200 - 50800)*0.25) + ((50800 - 13350)*0.15) + (13350*0.1))
        tax_percent = (tax_amount / income) * 100
        print('Tax amount owed by head of household filing status with', income,'dollar income is:\nOUTPUT', tax_amount)
        print('The percent of income paid in taxes is:\nOUTPUT',round(tax_percent,2))   
    
else:
    print('sorry, that''s not an option')