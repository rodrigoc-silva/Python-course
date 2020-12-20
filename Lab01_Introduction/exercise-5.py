
#This program calculates monthly and total payment.

#input
annualInterest = float(input('Enter annual interest rate:')) / 100
numberOfYears = int(input('Enter number of year:'))
loanAmount = float(input('Enter loan amount:'))
monthlyInterest = annualInterest / 12

#calculation
monthlyPayment = loanAmount * monthlyInterest / (1 - 1 / (1 + monthlyInterest) ** (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

#output
print('The monthly payment is ', format(monthlyPayment, ',.2f'))
print('The totla payment is', format(totalPayment, ',.2f'))

#ask user to quit program
input("\n\nPress any key to quit...")

##Output with 5 test cases
##
##Test Case 1.
##
# Enter annual interest rate:4.5
# Enter number of year:30
# Enter loan amount:350000.50
# The monthly payment is  1,773.40
# The totla payment is 638,424.40


# Press any key to quit...
##
##Test Case 2.
##
# Enter annual interest rate:7.25
# Enter number of year:5
# Enter loan amount:120000.95
# The monthly payment is  2,390.34
# The totla payment is 143,420.54


# Press any key to quit...
##
##Test Case 3.
##
# Enter annual interest rate:3.5
# Enter number of year:7
# Enter loan amount:35000
# The monthly payment is  470.39
# The totla payment is 39,513.16


# Press any key to quit...
##
##Test Case 4.
##
# Enter annual interest rate:10.5
# Enter number of year:30
# Enter loan amount:185000
# The monthly payment is  1,692.27
# The totla payment is 609,216.37


# Press any key to quit...
##
##Test Case 5.
##
# Enter annual interest rate:20.4
# Enter number of year:5
# Enter loan amount:10450.75
# The monthly payment is  279.21
# The totla payment is 16,752.72


# Press any key to quit...












