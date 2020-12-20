
#Federal income comparison.

#input income
income = int(input('Enter income (no commas, negative value to quit):'))

#loop
while (income >= 0):

    if (income == 0):

        #define case 0
        tax_17 = 0
        tax_18 = 0
        diff = 0
        diff_percent = 0

        #output case 0
        print('Income:', income)
        print('2017 tax:', format(tax_17, '.2f'))
        print('2018 tax:', format(tax_18, '.2f'))
        print('Difference:', format(diff, '.2f'))
        print('Difference (percent):', format(diff_percent, '.2f'))
        income = int(input('\nEnter income (no commas, negative value to quit):'))

    else:
        
        #past year range
        RANG1_OLD = 9325
        RANG2_OLD = 37950
        RANG3_OLD = 91900
        RANG4_OLD = 191650
        RANG5_OLD = 416700
        RANG6_OLD = 418400

        #current year range    
        RANG1_NEW = 9525
        RANG2_NEW = 38700
        RANG3_NEW = 82500
        RANG4_NEW = 157500
        RANG5_NEW = 200000
        RANG6_NEW = 500000

        #past year income calculation
        if (income <= RANG1_OLD):
            tax_17 = income * 0.1

        elif (income <= RANG2_OLD):
            tax_17 = (income - RANG1_OLD) * 0.15 + RANG1_OLD * 0.1

        elif (income <= RANG3_OLD):
            tax_17 = (income - RANG2_OLD) * 0.25 + (RANG2_OLD - RANG1_OLD) * 0.15 + RANG1_OLD * 0.1

        elif (income <= RANG4_OLD):
            tax_17 = (income - RANG3_OLD) * 0.28 + (RANG3_OLD - RANG2_OLD) * 0.25 + (RANG2_OLD - RANG1_OLD) * 0.15 + RANG1_OLD * 0.1

        elif (income <= RANG5_OLD):
            tax_17 = (income - RANG4_OLD) * 0.33 + (RANG4_OLD - RANG3_OLD) * 0.28 + (RANG3_OLD - RANG2_OLD) * 0.25 + (RANG2_OLD - RANG1_OLD) * 0.15 + RANG1_OLD * 0.1

        elif (income <= RANG6_OLD):
            tax_17 = (income - RANG5_OLD) * 0.35 + (RANG5_OLD - RANG4_OLD) * 0.33 + (RANG4_OLD - RANG3_OLD) * 0.28 + (RANG3_OLD - RANG2_OLD) * 0.25 + (RANG2_OLD - RANG1_OLD) * 0.15 + RANG1_OLD * 0.1

        else:
            tax_17 = (income - RANG6_OLD) * 0.396 + (RANG6_OLD - RANG5_OLD) * 0.35 + (RANG5_OLD - RANG4_OLD) * 0.33 + (RANG4_OLD - RANG3_OLD) * 0.28 + (RANG3_OLD - RANG2_OLD) * 0.25 + (RANG2_OLD - RANG1_OLD) * 0.15 + RANG1_OLD * 0.1

        #current year income calculation
        if (income <= RANG1_NEW):
            tax_18 = income * 0.1

        elif (income <= RANG2_NEW):
            tax_18 = (income - RANG1_NEW) * 0.12 + RANG1_NEW * 0.1

        elif (income <= RANG3_NEW):
            tax_18 = (income - RANG2_NEW) * 0.22 + (RANG2_NEW - RANG1_NEW) * 0.12 + RANG1_NEW * 0.1

        elif (income <= RANG4_NEW):
            tax_18 = (income - RANG3_NEW) * 0.24 + (RANG3_NEW - RANG2_NEW) * 0.22 + (RANG2_NEW - RANG1_NEW) * 0.12 + RANG1_NEW * 0.1

        elif (income <= RANG5_NEW):
            tax_18 = (income - RANG4_NEW) * 0.32 + (RANG4_NEW - RANG3_NEW) * 0.24 + (RANG3_NEW - RANG2_NEW) * 0.22 + (RANG2_NEW - RANG1_NEW) * 0.12 + RANG1_NEW * 0.1

        elif (income <= RANG6_NEW):
            tax_18 = (income - RANG5_NEW) * 0.35 + (RANG5_NEW - RANG4_NEW) * 0.32 + (RANG4_NEW - RANG3_NEW) * 0.24 + (RANG3_NEW - RANG2_NEW) * 0.22 + (RANG2_NEW - RANG1_NEW) * 0.12 + RANG1_NEW * 0.1

        else:
            tax_18 = (income - RANG6_NEW) * 0.37 + (RANG6_NEW - RANG5_NEW) * 0.35 + (RANG5_NEW - RANG4_NEW) * 0.32 + (RANG4_NEW - RANG3_NEW) * 0.24 + (RANG3_NEW - RANG2_NEW) * 0.22 + (RANG2_NEW - RANG1_NEW) * 0.12 + RANG1_NEW * 0.1

        #difference calculation
        diff = tax_18 - tax_17

        if (diff < 0):
            diff_percent = diff / tax_17 * 100 * -1
            
        else:
            diff_percent = diff / tax_17 * 100

        #output
        print('Income:', income)
        print('2017 tax:', format(tax_17, '.2f'))
        print('2018 tax:', format(tax_18, '.2f'))
        print('Difference:', format(diff, '.2f'))
        print('Difference (percent):', format(diff_percent, '.2f'))
        income = int(input('\nEnter income (no commas, negative value to quit):'))

#final output
input('\nThanks for using Federal Income Comparison Program!')


# case 1

# Enter income (no commas, negative value to quit):8000
# Income: 8000
# 2017 tax: 800.00
# 2018 tax: 800.00
# Difference: 0.00
# Difference (percent): 0.00

# Enter income (no commas, negative value to quit):15000
# Income: 15000
# 2017 tax: 1783.75
# 2018 tax: 1609.50
# Difference: -174.25
# Difference (percent): 9.77

# Enter income (no commas, negative value to quit):40000
# Income: 40000
# 2017 tax: 5738.75
# 2018 tax: 4739.50
# Difference: -999.25
# Difference (percent): 17.41

# Enter income (no commas, negative value to quit):100000
# Income: 100000
# 2017 tax: 20981.75
# 2018 tax: 18289.50
# Difference: -2692.25
# Difference (percent): 12.83

# Enter income (no commas, negative value to quit):200000
# Income: 200000
# 2017 tax: 49399.25
# 2018 tax: 45689.50
# Difference: -3709.75
# Difference (percent): 7.51

# Enter income (no commas, negative value to quit):500000
# Income: 500000
# 2017 tax: 153818.85
# 2018 tax: 150689.50
# Difference: -3129.35
# Difference (percent): 2.03

# Enter income (no commas, negative value to quit):1000000
# Income: 1000000
# 2017 tax: 351818.85
# 2018 tax: 335689.50
# Difference: -16129.35
# Difference (percent): 4.58

# Enter income (no commas, negative value to quit):10000000
# Income: 10000000
# 2017 tax: 3915818.85
# 2018 tax: 3665689.50
# Difference: -250129.35
# Difference (percent): 6.39

# Enter income (no commas, negative value to quit):-1

# Thanks for using Federal Income Comparison Program!


# case 2

# Enter income (no commas, negative value to quit):-1

# Thanks for using Federal Income Comparison Program!    


# case 3

# Enter income (no commas, negative value to quit):0
# Income: 0
# 2017 tax: 0.00
# 2018 tax: 0.00
# Difference: 0.00
# Difference (percent): 0.00

# Enter income (no commas, negative value to quit):10000
# Income: 10000
# 2017 tax: 1033.75
# 2018 tax: 1009.50
# Difference: -24.25
# Difference (percent): 2.35

# Enter income (no commas, negative value to quit):-10000

# Thanks for using Federal Income Comparison Program!


# case 4

# Enter income (no commas, negative value to quit):9525
# Income: 9525
# 2017 tax: 962.50
# 2018 tax: 952.50
# Difference: -10.00
# Difference (percent): 1.04

# Enter income (no commas, negative value to quit):38700
# Income: 38700
# 2017 tax: 5413.75
# 2018 tax: 4453.50
# Difference: -960.25
# Difference (percent): 17.74

# Enter income (no commas, negative value to quit):82500
# Income: 82500
# 2017 tax: 16363.75
# 2018 tax: 14089.50
# Difference: -2274.25
# Difference (percent): 13.90

# Enter income (no commas, negative value to quit):157500
# Income: 157500
# 2017 tax: 37081.75
# 2018 tax: 32089.50
# Difference: -4992.25
# Difference (percent): 13.46

# Enter income (no commas, negative value to quit):200000
# Income: 200000
# 2017 tax: 49399.25
# 2018 tax: 45689.50
# Difference: -3709.75
# Difference (percent): 7.51

# Enter income (no commas, negative value to quit):500000
# Income: 500000
# 2017 tax: 153818.85
# 2018 tax: 150689.50
# Difference: -3129.35
# Difference (percent): 2.03

# Enter income (no commas, negative value to quit):600000
# Income: 600000
# 2017 tax: 193418.85
# 2018 tax: 187689.50
# Difference: -5729.35
# Difference (percent): 2.96

# Enter income (no commas, negative value to quit):-1

# Thanks for using Federal Income Comparison Program!


# case 5

# Enter income (no commas, negative value to quit):9325
# Income: 9325
# 2017 tax: 932.50
# 2018 tax: 932.50
# Difference: 0.00
# Difference (percent): 0.00

# Enter income (no commas, negative value to quit):37950
# Income: 37950
# 2017 tax: 5226.25
# 2018 tax: 4363.50
# Difference: -862.75
# Difference (percent): 16.51

# Enter income (no commas, negative value to quit):91900
# Income: 91900
# 2017 tax: 18713.75
# 2018 tax: 16345.50
# Difference: -2368.25
# Difference (percent): 12.66

# Enter income (no commas, negative value to quit):191650
# Income: 191650
# 2017 tax: 46643.75
# 2018 tax: 43017.50
# Difference: -3626.25
# Difference (percent): 7.77

# Enter income (no commas, negative value to quit):416700
# Income: 416700
# 2017 tax: 120910.25
# 2018 tax: 121534.50
# Difference: 624.25
# Difference (percent): 0.52

# Enter income (no commas, negative value to quit):418400
# Income: 418400
# 2017 tax: 121505.25
# 2018 tax: 122129.50
# Difference: 624.25
# Difference (percent): 0.51

# Enter income (no commas, negative value to quit):518400
# Income: 518400
# 2017 tax: 161105.25
# 2018 tax: 157497.50
# Difference: -3607.75
# Difference (percent): 2.24

# Enter income (no commas, negative value to quit):-1

# Thanks for using Federal Income Comparison Program!
