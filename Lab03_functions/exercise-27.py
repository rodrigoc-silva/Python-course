
#This program shows the sum of all the single digit numbers entered in the string

def main():
    #get a string of numbers as input from user
    number_string = int(input('Enter a sequence of digits with nothing separating then: '))

    #call string_total method, and store the total
    total = string_total(number_string)

    #display the total
    print('The total of the digits in the string you entered is', total)


def string_total(number_string:int) -> (int):
    '''sepate the digits from the number and then sum them'''
    total = 0

    #define loop 
    while (number_string > 0):

        #calculate the next digit to add and execute the sum
        digit = number_string % 10
        total += digit

        #return the number with the digit used extracted
        number_string //= 10
        
    return total


if __name__=="__main__":
    main()

# case 1
# Enter a sequence of digits with nothing separating then: 4563
# The total of the digits in the string you entered is 18

# case 2
# Enter a sequence of digits with nothing separating then: 0
# The total of the digits in the string you entered is 0

# case 3
# Enter a sequence of digits with nothing separating then: -123
# The total of the digits in the string you entered is 0

# case 4
# Enter a sequence of digits with nothing separating then: 123456
# The total of the digits in the string you entered is 21

# case 5
# Enter a sequence of digits with nothing separating then: 01234
# The total of the digits in the string you entered is 10