
#Stock transaction program. It shows profit / loss amount.

#input
nameStock = input('Enter stock name:')
numberShare = float(input('Enter number of share:'))
stkPurchasePrice = float(input('Enter purchase price:'))
stkSellPrice = float(input('Enter selling price:'))
commission = float(input('Enter commision:'))

#caculation
amtPaid = numberShare * stkPurchasePrice
commissionPurchase = amtPaid * commission
amtSold = numberShare * stkSellPrice
commissionSell = amtSold * commission
ProfitLoss = (amtSold - commissionSell) - (amtPaid + commissionPurchase)

#output
print('Stock Name: ', nameStock)
print('Amount paid for the stock:      $', format(amtPaid, ',.2f'))
print('Commision paid on the purchase: $', format(commissionPurchase, ',.2f'))
print('Amount the stock sold for:      $', format(amtSold, ',.2f'))
print('Commision paid on the sale:     $', format(commissionSell, ',.2f'))
print('Profit (or loss if negative):   $', format(ProfitLoss, ',.2f'))

#ask user to quit program
input("\n\nPress any key to quit...")

##Output with 5 test cases
##
##Test Case 1.
##
# Enter stock name:Kaplack, Inc.
# Enter number of share:10000
# Enter purchase price:33.92
# Enter selling price:35.92
# Enter commision:0.04
# Stock Name:  Kaplack, Inc.

# Amount paid for the stock:      $ 339,200.00
# Commision paid on the purchase: $ 13,568.00
# Amount the stoco sold for:      $ 359,200.00
# Commision paid on the sale:     $ 14,368.00
# Profit (or loss if negative):   $ -7,936.00


# Press any key to quit...

# Test Case 2

# Enter stock name:IBM
# Enter number of share:20000
# Enter purchase price:97.85
# Enter selling price:101.02
# Enter commision:0.05
# Stock Name:  IBM

# Amount paid for the stock:      $ 1,957,000.00
# Commision paid on the purchase: $ 97,850.00
# Amount the stoco sold for:      $ 2,020,400.00
# Commision paid on the sale:     $ 101,020.00
# Profit (or loss if negative):   $ -135,470.00


# Press any key to quit...

# Test Case 3

# Enter stock name:Apple
# Enter number of share:125.75
# Enter purchase price:72.50
# Enter selling price:122.33
# Enter commision:0.07
# Stock Name:  Apple

# Amount paid for the stock:      $ 9,116.88
# Commision paid on the purchase: $ 638.18
# Amount the stoco sold for:      $ 15,383.00
# Commision paid on the sale:     $ 1,076.81
# Profit (or loss if negative):   $ 4,551.13


# Press any key to quit...

# Test Case 4

# Enter stock name:Tesla
# Enter number of share:5500
# Enter purchase price:12.99
# Enter selling price:21.35
# Enter commision:0.03
# Stock Name:  Tesla

# Amount paid for the stock:      $ 71,445.00
# Commision paid on the purchase: $ 2,143.35
# Amount the stoco sold for:      $ 117,425.00
# Commision paid on the sale:     $ 3,522.75
# Profit (or loss if negative):   $ 40,313.90


# Press any key to quit...

# Test Case 5

# Enter stock name:Google
# Enter number of share:4750.25
# Enter purchase price:102.72
# Enter selling price:103.34
# Enter commision:0.02
# Stock Name:  Google

# Amount paid for the stock:      $ 487,945.68
# Commision paid on the purchase: $ 9,758.91
# Amount the stoco sold for:      $ 490,890.84
# Commision paid on the sale:     $ 9,817.82
# Profit (or loss if negative):   $ -16,631.58


# Press any key to quit...
