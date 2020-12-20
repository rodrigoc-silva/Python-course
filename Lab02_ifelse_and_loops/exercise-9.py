
#This program shows if a number is even or odd.

#input
num = int(input("Enter any number:"))

#output
if (num % 2 == 0):
    print(num, "is even")
else:
    print(num, "is odd")
    
#ask user to quit program
input("\nPress any key to quit...")
    
# Case 1
# Enter any number:125
# 125 is odd

# Press any key to quit...

# Case 2
# Enter any number:0
# 0 is even

# Press any key to quit...

# Case 3
# Enter any number:1
# 1 is odd

# Press any key to quit...

# Case 4
# Enter any number:999999999
# 999999999 is odd

# Press any key to quit...

# Case 5
# Enter any number:99999998
# 99999998 is even

# Press any key to quit...
