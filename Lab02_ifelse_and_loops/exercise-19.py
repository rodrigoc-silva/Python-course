
#Stock transaction program. It shows profit / loss amount (using while loop).

#input
nameStock = input('Enter stock name (type "none" to quit):')

while (nameStock != 'none'):
    
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
    print('\nStock Name: ', nameStock)
    print('Amount paid for the stock:      $', format(amtPaid, '10,.2f'))
    print('Commision paid on the purchase: $', format(commissionPurchase, '10,.2f'))
    print('Amount the stock sold for:      $', format(amtSold, '10,.2f'))
    print('Commision paid on the sale:     $', format(commissionSell, '10,.2f'))
    print('Profit (or loss if negative):   $', format(ProfitLoss, '10,.2f'))

    #input next stock
    nameStock = input('\nEnter stock name (type "none" to quit):')


#quit program
input("\n\nProgram finished. Press any key...")


# case 1

# Enter stock name (type "none" to quit):Kaplac, inc.
# Enter number of share:10000
# Enter purchase price:33.92
# Enter selling price:35.92
# Enter commision:0.04

# Stock Name:  Kaplac, inc.
# Amount paid for the stock:      $ 339,200.00
# Commision paid on the purchase: $  13,568.00
# Amount the stock sold for:      $ 359,200.00
# Commision paid on the sale:     $  14,368.00
# Profit (or loss if negative):   $  -7,936.00

# Enter stock name (type "none" to quit):none


# Program finished. Press any key...


# case 2

# Enter stock name (type "none" to quit):IBM
# Enter number of share:2000
# Enter purchase price:97.85
# Enter selling price:99.02
# Enter commision:0.05

# Stock Name:  IBM
# Amount paid for the stock:      $ 195,700.00
# Commision paid on the purchase: $   9,785.00
# Amount the stock sold for:      $ 198,040.00
# Commision paid on the sale:     $   9,902.00
# Profit (or loss if negative):   $ -17,347.00

# Enter stock name (type "none" to quit):Apple
# Enter number of share:125.75
# Enter purchase price:72.50
# Enter selling price:122.33
# Enter commision:0.07

# Stock Name:  Apple
# Amount paid for the stock:      $   9,116.88
# Commision paid on the purchase: $     638.18
# Amount the stock sold for:      $  15,383.00
# Commision paid on the sale:     $   1,076.81
# Profit (or loss if negative):   $   4,551.13

# Enter stock name (type "none" to quit):none


# Program finished. Press any key...


# case 3

# Enter stock name (type "none" to quit):Tesla
# Enter number of share:5500
# Enter purchase price:12.99
# Enter selling price:21.35
# Enter commision:0.03

# Stock Name:  Tesla
# Amount paid for the stock:      $  71,445.00
# Commision paid on the purchase: $   2,143.35
# Amount the stock sold for:      $ 117,425.00
# Commision paid on the sale:     $   3,522.75
# Profit (or loss if negative):   $  40,313.90

# Enter stock name (type "none" to quit):Google
# Enter number of share:4750.25
# Enter purchase price:102.72
# Enter selling price:103.34
# Enter commision:0.02

# Stock Name:  Google
# Amount paid for the stock:      $ 487,945.68
# Commision paid on the purchase: $   9,758.91
# Amount the stock sold for:      $ 490,890.84
# Commision paid on the sale:     $   9,817.82
# Profit (or loss if negative):   $ -16,631.58

# Enter stock name (type "none" to quit):Amazon
# Enter number of share:751.50
# Enter purchase price:99.35
# Enter selling price:100.98
# Enter commision:0.03

# Stock Name:  Amazon
# Amount paid for the stock:      $  74,661.52
# Commision paid on the purchase: $   2,239.85
# Amount the stock sold for:      $  75,886.47
# Commision paid on the sale:     $   2,276.59
# Profit (or loss if negative):   $  -3,291.49

# Enter stock name (type "none" to quit):none


# Program finished. Press any key...


# case 4

# Enter stock name (type "none" to quit):none


# Program finished. Press any key...


# case 5

# Enter stock name (type "none" to quit):Cocacola
# Enter number of share:10000
# Enter purchase price:57.79
# Enter selling price:157.79
# Enter commision:0.1

# Stock Name:  Cocacola
# Amount paid for the stock:      $ 577,900.00
# Commision paid on the purchase: $  57,790.00
# Amount the stock sold for:      $ 1,577,900.00
# Commision paid on the sale:     $ 157,790.00
# Profit (or loss if negative):   $ 784,420.00

# Enter stock name (type "none" to quit):Gillete
# Enter number of share:10000
# Enter purchase price:120.45
# Enter selling price:1.19
# Enter commision:0.02

# Stock Name:  Gillete
# Amount paid for the stock:      $ 1,204,500.00
# Commision paid on the purchase: $  24,090.00
# Amount the stock sold for:      $  11,900.00
# Commision paid on the sale:     $     238.00
# Profit (or loss if negative):   $ -1,216,928.00

# Enter stock name (type "none" to quit):none


# Program finished. Press any key...
