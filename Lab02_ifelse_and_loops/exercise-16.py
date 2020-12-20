
#This program calculates the sum of integers.

total = 0
count_num = int(input("How many numbers do you want to add?"))

for numb in range (count_num):
    print("Enter number", numb + 1, end='')
    value = int(input(":"))
    total = total + value
print("The total is", format(total, '.1f'))

input("\nPress any key to quit")

# Case 1
# How many numbers do you want to add?3
# Enter number 1:25
# Enter number 2:34
# Enter number 3:33
# The total is 92.0

# Press any key to quit

# Case 2
# How many numbers do you want to add?2
# Enter number 1:99
# Enter number 2:1
# The total is 100.0

# Press any key to quit

# Case 3
# How many numbers do you want to add?3
# Enter number 1:10
# Enter number 2:20
# Enter number 3:-30
# The total is 0.0

# Press any key to quit

# Case 4
# How many numbers do you want to add?5
# Enter number 1:12
# Enter number 2:23
# Enter number 3:34
# Enter number 4:45
# Enter number 5:56
# The total is 170.0

# Press any key to quit

# Case 5
# How many numbers do you want to add?5
# Enter number 1:-12
# Enter number 2:-23
# Enter number 3:-34
# Enter number 4:-45
# Enter number 5:-56
# The total is -170.0

# Press any key to quit