
#This program shows if the person is eligible to vote.

#input
age = int(input("Enter the age:"))

#output
if (age >= 18):
    print("You are eligible to vote")
else:
    print("You have to wait for another", 18 - age, "years to cast your vote")

#ask user to quit program
input("\nPress any key to quit...")

#Case 1
#Enter the age:10
#You have to wait for another 8 years to cast your vote

#Press any key to quit...

# Case 2
# Enter the age:18
# You are eligible to vote

# Press any key to quit...

# Case 3
# Enter the age:17
# You have to wait for another 1 years to cast your vote

# Press any key to quit...

# Case 4
# Enter the age:19
# You are eligible to vote

# Press any key to quit...

# Case 5
# Enter the age:0
# You have to wait for another 18 years to cast your vote

# Press any key to quit...