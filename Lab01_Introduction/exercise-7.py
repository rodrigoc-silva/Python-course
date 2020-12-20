
#This program calculates the bill amount.

#input
qtdSold = float(input('Enter the quantity of item sold:'))
valItem = float(input('Enter the value of item:'))
discount = float(input('Enter the discount percentage:'))
tax = float(input('Enter the tax:'))

#calculation
amount = qtdSold * valItem
discountAmt = amount * discount / 100
subTotal = amount - discountAmt
taxAmt = subTotal * tax / 100
total = subTotal + taxAmt

#output
print('')
print('**********BILL**********')
print('Quantity sold:', format(qtdSold, '21,.2f'))
print('Price per item:', format(valItem, '20,.2f'))
print('')
print(20 * ' ', 15 * '-')
print('Amount:', format(amount, '28,.2f'))
print('Discount:', 10 * ' ', '-', format(discountAmt, '13,.2f'))
print(20 * ' ', 15 * '-')
print('Discount Total:', format(subTotal, '20,.2f'))
print('Tax:', 15 * ' ', '+', format(taxAmt, '13,.2f'))
print(20 * ' ', 15 * '-')
print('Total amount to be paid: $', format(total, '9,.2f'))

#ask user to quit program
input("\n\nPress any key to quit...")

##Output with 5 test cases
##
##Test Case 1
##
# Enter the quantity of item sold:80
# Enter the value of item:100
# Enter the discount percentage:10
# Enter the tax:14

# **********BILL**********
# Quantity sold:                 80.00
# Price per item:               100.00

                     # ---------------
# Amount:                     8,000.00
# Discount:            -        800.00
                     # ---------------
# Discount Total:             7,200.00
# Tax:                 +      1,008.00
                     # ---------------
# Total amount to be paid: $  8,208.00


# Press any key to quit...

#Test Case 2

# Enter the quantity of item sold:10
# Enter the value of item:1
# Enter the discount percentage:0
# Enter the tax:0

# **********BILL**********
# Quantity sold:                 10.00
# Price per item:                 1.00

                     # ---------------
# Amount:                        10.00
# Discount:            -          0.00
                     # ---------------
# Discount Total:                10.00
# Tax:                 +          0.00
                     # ---------------
# Total amount to be paid: $     10.00


# Press any key to quit...

#Test Case 3

# Enter the quantity of item sold:12.35
# Enter the value of item:7.99
# Enter the discount percentage:5.5
# Enter the tax:7.4

# **********BILL**********
# Quantity sold:                 12.35
# Price per item:                 7.99

                     # ---------------
# Amount:                        98.68
# Discount:            -          5.43
                     # ---------------
# Discount Total:                93.25
# Tax:                 +          6.90
                     # ---------------
# Total amount to be paid: $    100.15


# Press any key to quit...

#Test Case 4

# Enter the quantity of item sold:1000000
# Enter the value of item:2.35
# Enter the discount percentage:7
# Enter the tax:7

# **********BILL**********
# Quantity sold:          1,000,000.00
# Price per item:                 2.35

                     # ---------------
# Amount:                 2,350,000.00
# Discount:            -    164,500.00
                     # ---------------
# Discount Total:         2,185,500.00
# Tax:                 +    152,985.00
                     # ---------------
# Total amount to be paid: $ 2,338,485.00


# Press any key to quit...

#Test Case 5

# Enter the quantity of item sold:10
# Enter the value of item:100
# Enter the discount percentage:100
# Enter the tax:7

# **********BILL**********
# Quantity sold:                 10.00
# Price per item:               100.00

                     # ---------------
# Amount:                     1,000.00
# Discount:            -      1,000.00
                     # ---------------
# Discount Total:                 0.00
# Tax:                 +          0.00
                     # ---------------
# Total amount to be paid: $      0.00


# Press any key to quit...
