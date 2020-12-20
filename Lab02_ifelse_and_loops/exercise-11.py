
#This program shows if the input is a number or a lowercase or
#uppercase character.   

#input
character = input("Enter any character:")

#output
if (character >= '0' and character <= '9'):
    print("A number was entered")
elif (character >= 'A' and character <= 'Z'):
    print("A uppercase character was entered")
elif (character >= 'a' and character <= 'z'):
    print("A lowercase character was entered")
else:
    print("Invalid character entered")

#ask to user to quit program
input("\nPress any key to quit...")

# Case 1
# Enter any character:C
# A uppercase character was entered

# Press any key to quit...

# Case 2
# Enter any character:a
# A lowercase character was entered

# Press any key to quit...

# Case 3
# Enter any character:5
# A number was entered

# Press any key to quit...

# Case 4
# Enter any character:"
# Invalid character entered

# Press any key to quit...

# Case 5
# Enter any character:Z
# A uppercase character was entered

# Press any key to quit...