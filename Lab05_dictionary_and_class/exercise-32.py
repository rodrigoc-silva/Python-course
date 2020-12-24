
#This program shows 5 functions about dictionary
#print key, value, key-value, key-value ascending, and average

def main():
    #define dictionary
    grade = {"A":8, "D":3, "B":15, "F":2, "C":6}
    #call functions
    print_keys(grade)
    #print a blank line
    print()
    print_values(grade)
    print()
    print_dict(grade)
    print()
    print_dict_ascend(grade)
    print()
    print_avg(grade)


def print_keys(grade:dict) -> None:
    '''This function prints the keys of the dictionary'''
    #loop for each key
    for key in grade:
        print(key)


def print_values(grade:dict) -> None:
    '''This function prints the values of the dictionary'''
    #loop for each value
    for value in grade.values():
        print(value)


def print_dict(grade:dict) -> None:
    '''This function prints the key-values of the dictionary'''
    #loop for each key
    for key in grade:
        #print key and value
        print(key, grade[key])


def print_dict_ascend(grade:dict) -> None:
    '''This function prints the key-values of the dictionary
    in ascending order'''
    #loop for each key using sorted method
    for key in sorted(grade):
        print(key, grade[key])

 
def print_avg(grade:dict) -> None:
    '''This function calculates the average of the values
    and print it'''
    #define variable
    sum = 0
    #loop for each value
    for value in grade.values():
        #calculate the sum
        sum += int(value)
    #calcualte the average
    avg = sum / len(grade)
    #output
    print("The average is:", avg)
        

#call the main function
if __name__=="__main__":   
    main()


# case 1
# A
# D
# B
# F
# C

# 8
# 3
# 15
# 2
# 6

# A 8
# D 3
# B 15
# F 2
# C 6

# A 8
# B 15
# C 6
# D 3
# F 2

# The average is: 6.8

# case 2
# E
# D
# C
# B
# A

# 1
# 2
# 3
# 4
# 5

# E 1
# D 2
# C 3
# B 4
# A 5

# A 5
# B 4
# C 3
# D 2
# E 1

# The average is: 3.0

# case 3
# a
# b
# c
# B
# A

# 1
# 2
# 3
# 4
# 5

# a 1
# b 2
# c 3
# B 4
# A 5

# A 5
# B 4
# a 1
# b 2
# c 3

# The average is: 3.0

# case 4
# A
# C
# B

# 5.1
# 2.1
# 4.5

# A 5.1
# C 2.1
# B 4.5

# A 5.1
# B 4.5
# C 2.1

# The average is: 3.6666666666666665

# case 5
# D
# B
# C
# A
# F

# 12
# 21
# 34
# 4
# 5

# D 12
# B 21
# C 34
# A 4
# F 5

# A 4
# B 21
# C 34
# D 12
# F 5

# The average is: 15.2