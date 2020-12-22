
# This program calculates a salesperson's pay

def main():
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    comm_rate = determine_comm_rate(sales)
    # Calculate the pay.
    pay = sales * comm_rate - advanced_pay
    # Determine whether the pay is negative.
    if (pay < 0):
        print('The pay is $', format(pay, ',.2f'), sep='')
        print('The salesperson must reimburse')
        print('the company.')

    else:
        # Display the amount of pay.
        print('The pay is $', format(pay, ',.2f'), sep='')


def get_sales() -> (float):
    '''Get the amount of sales from user'''
    sales = float(input('Enter the monthly sales: '))
    return sales


def get_advanced_pay() -> (float):
    '''Get the amount of advanced pay from user'''
    print('Enter the amount of advanced pay, or')
    print('enter 0 if no advanced pay was given.')
    advanced_pay = float(input('Advanced pay: '))
    return advanced_pay


def determine_comm_rate(sales:float) -> (float):
    '''Determine the commission rate'''
    if (sales > 21999.99):
        comm_rate = 0.18
    elif (sales >= 18000.00):
        comm_rate = 0.16
    elif (sales >= 15000.00):
        comm_rate = 0.14
    elif (sales >= 10000.00):
        comm_rate = 0.12
    elif (sales < 10000.00):
        comm_rate = 0.1
    return comm_rate


if __name__=="__main__":
    main()

# case 1
# Enter the monthly sales:14550.00
# Enter the amount of advanced pay, or
# enter 0 if no advanced pay was given.
# Advanced pay:1000.00
# The pay is $746.00

# case 2
# Enter the monthly sales:9500
# Enter the amount of advanced pay, or
# enter 0 if no advanced pay was given.
# Advanced pay:0
# The pay is $950.00

# case 3
# Enter the monthly sales:12000.00
# Enter the amount of advanced pay, or
# enter 0 if no advanced pay was given.
# Advanced pay:2000.00
# The pay is $-560.00
# The salesperson must reimburse
# the company.

# case 4
# Enter the monthly sales:22000.00
# Enter the amount of advanced pay, or
# enter 0 if no advanced pay was given.
# Advanced pay:1000
# The pay is $2,960.00

# case 5
# Enter the monthly sales:17500
# Enter the amount of advanced pay, or
# enter 0 if no advanced pay was given.
# Advanced pay:2450
# The pay is $0.00
