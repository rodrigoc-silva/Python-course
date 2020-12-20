
#This program shows if a character is vowel or not.

#input
character = input("Enter any character: ")

#output
if (character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u'):
    print(character, "is a vowel")
elif (character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U'):
    print(character, "is a vowel")
else:
    print(character, "is not a vowel")

#ask to user to quit program
input("\nPress any key to quit...")

# Case 1
# Enter any character: h
# h is not a vowel

# Press any key to quit...

# Case 2
# Enter any character: a
# a is a vowel

# Press any key to quit...

# Case 3
# Enter any character: U
# U is a vowel

# Press any key to quit...

# Case 4
# Enter any character: z
# z is not a vowel

# Press any key to quit...

# Case 5
# Enter any character: H
# H is not a vowel

# Press any key to quit...