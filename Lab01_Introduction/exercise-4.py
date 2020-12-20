
#This program shows the amount of each ingredient needed for a numbers of cookies.

#constants
sugar = 1.5
butter = 1
flour = 2.75
cookies = 48

#input
numOfCookies = int(input('Enter the number of cookies:'))

#calculation
amtSugar = sugar / cookies * numOfCookies
amtButter = butter / cookies * numOfCookies
amtFlour = flour / cookies * numOfCookies

#output
print('To make', numOfCookies, 'cookies, you will nedd:')
print(format(amtSugar, ',.2f'), 'cups of sugar.')
print(format(amtButter, ',.2f'),  'cups of butter.')
print(format(amtFlour, ',.2f'), 'cups of flour.')

#ask user to quit program
input("\n\nPress any key to quit...")

##Output with 5 test cases
##
##Test Case 1.
##
# Enter the number of cookies:56
# To make 56 cookies, you will nedd:
# 1.75 cups of sugar.
# 1.17 cups of butter.
# 3.21 cups of flour.
##
##
# Press any key to quit...
##
##Test Case 2.
##
# Enter the number of cookies:96
# To make 96 cookies, you will nedd:
# 3.00 cups of sugar.
# 2.00 cups of butter.
# 5.50 cups of flour.
##
##
# Press any key to quit...
##
##Test Case 3.
##
# Enter the number of cookies:480
# To make 480 cookies, you will nedd:
# 15.00 cups of sugar.
# 10.00 cups of butter.
# 27.50 cups of flour.
##
##
# Press any key to quit...
##
##Test Case 4.
##
# Enter the number of cookies:200
# To make 200 cookies, you will nedd:
# 6.25 cups of sugar.
# 4.17 cups of butter.
# 11.46 cups of flour.
##
##
# Press any key to quit...
##
##Test Case 5.
##
# Enter the number of cookies:2
# To make 2 cookies, you will nedd:
# 0.06 cups of sugar.
# 0.04 cups of butter.
# 0.11 cups of flour.
##
##
# Press any key to quit...







