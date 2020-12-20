
#This program calculates the retail price.

#declaration
MARKUP = 2.5
next_item = 'y'

#loop for next item
while (next_item == 'y' or next_item == 'Y'):
    whole_cost = float(input("Enter the item's wholesale cost:"))

#loop for check price
    if (whole_cost < 0):
        print("ERROR: The cost cannot be negative")
        whole_cost = float(input("Enter the correct wholesale cost:"))
        #calculation and output
        retail_price = whole_cost * MARKUP
        print("Retail price is $", format(retail_price, '.2f'))
        next_item = input("Do you have another item?(Enter y for yes):")
        print()
    else:
        #calculation and output
        retail_price = whole_cost * MARKUP
        print("Retail price is $", format(retail_price, '.2f'))
        next_item = input("Do you have another item?(Enter y for yes):")
        print()

# Case 1
# Enter the item's wholesale cost:-.50
# ERROR: The cost cannot be negative
# Enter the correct wholesale cost:.50
# Retail price is $ 1.25
# Do you have another item?(Enter y for yes):n

# Case 2
# Enter the item's wholesale cost:1.50
# Retail price is $ 3.75
# Do you have another item?(Enter y for yes):y

# Enter the item's wholesale cost:1.00
# Retail price is $ 2.50
# Do you have another item?(Enter y for yes):n

# Case 3
# Enter the item's wholesale cost:9.99
# Retail price is $ 24.98
# Do you have another item?(Enter y for yes):Y

# Enter the item's wholesale cost:-9.99
# ERROR: The cost cannot be negative
# Enter the correct wholesale cost:10.01
# Retail price is $ 25.02
# Do you have another item?(Enter y for yes):y

# Enter the item's wholesale cost:10.00
# Retail price is $ 25.00
# Do you have another item?(Enter y for yes):N

# Case 4
# Enter the item's wholesale cost:-2.50
# ERROR: The cost cannot be negative
# Enter the correct wholesale cost:2.50
# Retail price is $ 6.25
# Do you have another item?(Enter y for yes):y

# Enter the item's wholesale cost:-3.25
# ERROR: The cost cannot be negative
# Enter the correct wholesale cost:3.25
# Retail price is $ 8.12
# Do you have another item?(Enter y for yes):Y

# Enter the item's wholesale cost:-4.75
# ERROR: The cost cannot be negative
# Enter the correct wholesale cost:4.75
# Retail price is $ 11.88
# Do you have another item?(Enter y for yes):n

# Case 5
# Enter the item's wholesale cost:100.00
# Retail price is $ 250.00
# Do you have another item?(Enter y for yes):y

# Enter the item's wholesale cost:10.00
# Retail price is $ 25.00
# Do you have another item?(Enter y for yes):y

# Enter the item's wholesale cost:1.00
# Retail price is $ 2.50
# Do you have another item?(Enter y for yes):y

# Enter the item's wholesale cost:0
# Retail price is $ 0.00
# Do you have another item?(Enter y for yes):y

# Enter the item's wholesale cost:0.01
# Retail price is $ 0.03
# Do you have another item?(Enter y for yes):n

