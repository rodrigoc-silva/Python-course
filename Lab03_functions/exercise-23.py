
#This program calculates the simple interest.

def main():
    RATE = 0.01
    PERIODS = 10
    PRINCIPAL = 10000.00
    show_interest(RATE, PERIODS, PRINCIPAL)


def show_interest(RATE:float, PERIODS:int, PRINCIPAL:float) -> None:
    '''Calculate the simple interest and print out the result'''
    interest = RATE * PERIODS * PRINCIPAL
    print("The simple interest will be $", format(interest, ',.2f'))


if __name__=="__main__":
    main()


# case 1
# The simple interest will be $1,000.00

# case 2
# PRINCIPAL = -10000.00
# The simple interest will be $-1,000.00

# case 3
# PERIODS = 2
# The simple interest will be $200.00

# case 4
# RATE = 0.0
# The simple interest will be $0.00

# case 5
# PRINCIPAL = 1000000
# The simple interest will be $100,000.00
