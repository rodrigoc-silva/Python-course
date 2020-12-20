
#Lottery Game program

import random

#input
comp_num = random.randint(0, 99)
my_num = int(input("Enter a number 00 to 99 (-999 to quit):"))

#calculation to separate digits
firstC_dig = comp_num // 10
secC_dig =comp_num % 10
firstM_dig = my_num // 10
secM_dig = my_num % 10

#loop to use flag
while (my_num != -999):
    
    #define rules and prizes
    if (firstC_dig == firstM_dig and secC_dig == secM_dig):

        #output
        prize = 10000
        print()
        print("Congratulations! You won $", format(prize, ',.2f'))
        print()

        #input a new turn
        comp_num = random.randint(0, 99)
        my_num = int(input("Enter a number 00 to 99 (-999 to quit):"))

        firstC_dig = comp_num // 10
        secC_dig =comp_num % 10
        firstM_dig = my_num // 10
        secM_dig = my_num % 10

    elif (firstC_dig == secM_dig and secC_dig == firstM_dig):

        #output
        prize = 3000
        print()
        print("Congratulations! You won $", format(prize, ',.2f'))
        print()

        #input a new turn
        comp_num = random.randint(0, 99)
        my_num = int(input("Enter a number 00 to 99 (-999 to quit):"))

        firstC_dig = comp_num // 10
        secC_dig =comp_num % 10
        firstM_dig = my_num // 10
        secM_dig = my_num % 10

    elif (firstC_dig == firstM_dig or secC_dig == secM_dig or firstC_dig == secM_dig or secC_dig == firstM_dig):

        #output
        prize = 1000
        print()
        print("Congratulations! You won $", format(prize, ',.2f'))
        print()

        #input a new turn
        comp_num = random.randint(0, 99)
        my_num = int(input("Enter a number 00 to 99 (-999 to quit):"))

        firstC_dig = comp_num // 10
        secC_dig =comp_num % 10
        firstM_dig = my_num // 10
        secM_dig = my_num % 10
              
    else:

        #output
        print()
        print("Not this time!")
        print()

        #input a new turn
        comp_num = random.randint(0, 99)
        my_num = int(input("Enter a number 00 to 99 (-999 to quit):"))

        firstC_dig = comp_num // 10
        secC_dig =comp_num % 10
        firstM_dig = my_num // 10
        secM_dig = my_num % 10

#output after flag
print()
input("Thanks for playing")


# case 1

# Enter a number 00 to 99 (-999 to quit):12

# Not this time!

# Enter a number 00 to 99 (-999 to quit):23

# Not this time!

# Enter a number 00 to 99 (-999 to quit):34

# Not this time!

# Enter a number 00 to 99 (-999 to quit):45

# Not this time!

# Enter a number 00 to 99 (-999 to quit):56

# Not this time!

# Enter a number 00 to 99 (-999 to quit):-999

# Thanks for playing


# case 2

# Enter a number 00 to 99 (-999 to quit):00

# Not this time!

# Enter a number 00 to 99 (-999 to quit):01

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):02

# Not this time!

# Enter a number 00 to 99 (-999 to quit):03

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):04

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):05

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):-999

# Thanks for playing


# case 3

# Enter a number 00 to 99 (-999 to quit):56

# Not this time!

# Enter a number 00 to 99 (-999 to quit):56

# Congratulations! You won $ 3,000.00

# Enter a number 00 to 99 (-999 to quit):56

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):56

# Not this time!

# Enter a number 00 to 99 (-999 to quit):-999

# Thanks for playing


# case 4

# Enter a number 00 to 99 (-999 to quit):-999

# Thanks for playing


# case 5

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 10,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 3,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 3,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 1,000.00

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Not this time!

# Enter a number 00 to 99 (-999 to quit):98

# Congratulations! You won $ 10,000.00

# Enter a number 00 to 99 (-999 to quit):-999

# Thanks for playing
