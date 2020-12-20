
#This program prints the number of asterisks entered.
#input
stars = int(input("How many stars do you want?"))
count = 0
#calculation
while (count < stars):
    count += 1
#output
print()
print("*" * count)
#ask to quit
input("\nPress any key to quit...")

# Case 1
# How many stars do you want?20
# ********************

# Press any key to quit...

# Case 2
# How many stars do you want?1
# *

# Press any key to quit...

# Case 3
# How many stars do you want?-20


# Press any key to quit...

# Case 4
# How many stars do you want?10
# **********

# Press any key to quit...

# Case 5
# How many stars do you want?0


# Press any key to quit...
