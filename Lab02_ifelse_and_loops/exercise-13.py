
#This program calculates the property tax.

#constant declaration
TAX_FACTOR = 0.0065

#input
print("Enter the property lot number or enter -999 to end")
lot_num = int(input("Enter the lot number:"))

#loop
while (lot_num != -999 and lot_num != 0):
    property_value = float(input("Enter property value:"))
    #calculation
    property_tax = property_value * TAX_FACTOR
    #output
    print("Property tax: $", format(property_tax, '.2f'))
    print()
    print("Enter the property lot number or enter -999 to end")
    lot_num = int(input("Enter the lot number:"))

input("\nPress any key to quit...")

# Case 1
# Enter the property lot number or enter -999 to end
# Enter the lot number:100
# Enter property value:100000.00
# Property tax: $ 650.00

# Enter the property lot number or enter -999 to end
# Enter the lot number:200
# Enter property value:5000.00
# Property tax: $ 32.50

# Enter the property lot number or enter -999 to end
# Enter the lot number:-999

# Press any key to quit...

# Case 2
# Enter the property lot number or enter -999 to end
# Enter the lot number:1
# Enter property value:1000000.00
# Property tax: $ 6500.00

# Enter the property lot number or enter -999 to end
# Enter the lot number:2
# Enter property value:2000000.00
# Property tax: $ 13000.00

# Enter the property lot number or enter -999 to end
# Enter the lot number:0

# Press any key to quit...

# Case 3
# Enter the property lot number or enter -999 to end
# Enter the lot number:-999

# Press any key to quit...

# Case 4
# Enter the property lot number or enter -999 to end
# Enter the lot number:10
# Enter property value:250000
# Property tax: $ 1625.00

# Enter the property lot number or enter -999 to end
# Enter the lot number:20
# Enter property value:250000.00
# Property tax: $ 1625.00

# Enter the property lot number or enter -999 to end
# Enter the lot number:30
# Enter property value:250000.000
# Property tax: $ 1625.00

# Enter the property lot number or enter -999 to end
# Enter the lot number:40
# Enter property value:255555.55
# Property tax: $ 1661.11

# Enter the property lot number or enter -999 to end
# Enter the lot number:-999

# Press any key to quit...

# Case 5
# Enter the property lot number or enter -999 to end
# Enter the lot number:100
# Enter property value:1234567.89
# Property tax: $ 8024.69

# Enter the property lot number or enter -999 to end
# Enter the lot number:101
# Enter property value:99999.99
# Property tax: $ 650.00

# Enter the property lot number or enter -999 to end
# Enter the lot number:102
# Enter property value:-20000.00
# Property tax: $ -130.00

# Enter the property lot number or enter -999 to end
# Enter the lot number:103
# Enter property value:1000.00
# Property tax: $ 6.50

# Enter the property lot number or enter -999 to end
# Enter the lot number:0

# Press any key to quit...