
#This program define if a credit card number is valid or not valid

def main():

    #ask how many card number the user wants to enter
    countCards = int(input('How many card numbers do you want to enter? '))

    #loop for each card number
    for card in range(countCards):
        #input
        number = input('\nEnter a credit card number as a long integer: ')
        #define if card starts with a valid number
        if number.startswith('4') or number.startswith('5') or number.startswith('6') or number.startswith('37'):
        
            totalOdd = sumOfOddPlace(number)
            listEven = getDigit(number)
            totalEven = sumOfDoubleEvenPlace(listEven)
            cardValid = isValid(totalOdd, totalEven)
        
            #output if is a valid card or not
            if (cardValid == True):
                print(number, 'is valid')
            else:
                print(number, 'is invalid')

        else:
            print(number, 'is invalid')

    
def isValid(totalOdd:int, totalEven:int) -> bool:
    '''return if the car number is valid or not'''
    cardValid = False
    
    # check if sum of odd and even places is divisible per 10
    sumOfPlaces = totalOdd + totalEven
    
    if (sumOfPlaces % 10  == 0):
        cardValid = True
    else:
        cardValid = False

    return cardValid


def sumOfDoubleEvenPlace(listEven:list) -> int:
    '''Take the even place numbers and sum them'''
    totalEven = 0
    
    #sum each even place number
    for num in listEven:
        totalEven += num
        
    return totalEven


def getDigit(number:str) -> list:
    '''Return this number if it is a single digit, otherwise, return the sum of the two digits'''
    num = int(number)
    listEven = []

    #separate the even place numbers
    while (num > 0):
        digit = num % 100
        evenNum = digit // 10
        num //= 100
        evenNum *= 2

        #check if the number has 2 digits and sum them 
        if (evenNum < 10):
            listEven.append(evenNum)
        else:
            unEvenNum = evenNum % 10
            decEvenNum = evenNum // 10
            evenNum = decEvenNum + unEvenNum
            listEven.append(evenNum)
            
    return listEven
    
        
def sumOfOddPlace(number:str) -> int:
    '''sum the values in the odd places of the card number entered by user'''
    num = int(number)
    totalOdd = 0

    #separate the odd place numbers
    while (num > 0):
        digit = num % 10
        num //= 100
        totalOdd += digit
    
    return totalOdd


if __name__=="__main__":
    main()

# case 1
# How many card numbers do you want to enter? 2

# Enter a credit card number as a long integer: 4388576018402626
# 4388576018402626 is invalid

# Enter a credit card number as a long integer: 4388576018410707
# 4388576018410707 is valid

# case 2
# How many card numbers do you want to enter? 2

# Enter a credit card number as a long integer: 5391865110644053
# 5391865110644053 is valid

# Enter a credit card number as a long integer: 5392865110644564
# 5392865110644564 is invalid

# case 3
# How many card numbers do you want to enter? 0
# >>> 

# case 4
# How many card numbers do you want to enter? 1

# Enter a credit card number as a long integer: 6492315679084321
# 6492315679084321 is valid

# case 5
# How many card numbers do you want to enter? 4

# Enter a credit card number as a long integer: 6492315679084324
# 6492315679084324 is invalid

# Enter a credit card number as a long integer: 3754090057388
# 3754090057388 is invalid

# Enter a credit card number as a long integer: 3754090057380
# 3754090057380 is valid

# Enter a credit card number as a long integer: 2754090057381
# 2754090057381 is invalid

