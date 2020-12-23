
#Program to test functions a to j.

#define constant variables
ONE_TEN = [1, 3, 3, 15, 71, 9, 13, 5, 7, 9]

def main():
    
    print('The original data for all functions is:', ONE_TEN)
    
    #a. Demonstrate swapping the first and last element.
    data = list(ONE_TEN)
    swapFristLast(data)
    print("After swapping first and last: ", data)

    #b. Demonstrate shifting to the right.
    data = list(ONE_TEN)
    shiftRight(data)
    print('After shifting right:', data)

    #c. Demonstrate replacing even elements with zero.
    data = list(ONE_TEN)
    replaceEven(data)
    print('After replace even elements:', data)

    #d. Demonstrate replacing values with the larger of their neighbors.
    data = list(ONE_TEN)
    replaceNeighbors(data)
    print('After replacing with neighbors:', data)

    #e. Demonstrate removing the middle element.
    data = list(ONE_TEN)
    removeMiddle(data)
    print('After removing the middle element(s):', data)

    #f. Demonstrate moving even elements to the front of the list.
    data = list(ONE_TEN)
    evenToFront(data)
    print('After moving even elements:', data)

    #g. Demonstrate finding the second largest value.
    print('The second lagest value is:', secondLargest(ONE_TEN))

    #h. Demonstrate testing if the list is in increasing order.
    print('The list is in increasing order:', isIncreasing(ONE_TEN))

    #i. Demonstrate testing if the list contains adjacent duplicates.
    print('The list has adjacent duplicates:', hasAdjacentDuplicate(ONE_TEN))

    #j. Demonstrate testing if the list contains duplicates.
    print('The list has duplicates:', hasDuplicate(ONE_TEN))
    
    
    
    
def swapFristLast(data:list) -> None:
    '''This function swapps the first and last element'''
    first_data = data[0]
    last_data = data[-1]
    data[0] = last_data
    data[-1] = first_data


def shiftRight(data:list) -> None:
    '''This function shifts to the right'''
    last_data = data[-1]
    data.remove(last_data)
    data.insert(0, last_data)


def replaceEven(data:list) -> None:
    '''This function replaces even elements with zero'''
    for num in range(len(data)):

        if (data[num] % 2 == 0):
           data[num] = 0


def replaceNeighbors(data:list) -> None:
    '''this function replaces values with the larger of their neighbors'''
    for num in range(1, len(data)-1):

        if data[num - 1] > data[num + 1]:
            data[num] = data[num -1]

        else:
            data[num] = data[num +1]


def removeMiddle(data:list) -> None:
    '''This function removes the middle element'''
    data_lenght = len(data)
    middle_index = data_lenght//2

    if (data_lenght % 2 == 0):
        middle1 = data[middle_index]
        data.remove(middle1)
        middle2 = data[middle_index - 1]
        data.remove(middle2)

    else:
        middle1 = data[middle_index]
        data.remove(middle1)
        

def evenToFront(data:list) -> int:
    '''This function moves even elements to the front of the list'''
    count = 0

    for num in range(len(data)):
        if data[num] % 2 == 0:
            item = data[num]
            data.remove(item)
            data.insert(count, item)
            count += 1
        
        
def secondLargest(ONE_TEN:list) -> int:
    '''This function finds the second largest value'''
    higher = max(ONE_TEN)
    item_index = ONE_TEN.index(higher)
    ONE_TEN.remove(higher)
    sec_higher = max(ONE_TEN)
    ONE_TEN.insert(item_index, higher)
    
    return sec_higher


def isIncreasing(ONE_TEN:list) -> bool:
    '''this function tests if the list is in increasing order'''
    sorted_list = [] + ONE_TEN
    sorted_list.sort()

    if (sorted_list == ONE_TEN):
        return True

    else:
        return False
    

def hasAdjacentDuplicate(ONE_TEN:list) -> bool:
    '''This function tests if the list contains adjacent duplicates'''
    low_item = 1
    high_item = len(ONE_TEN)-2

    while (low_item <= high_item):

        if (ONE_TEN[low_item] == ONE_TEN[low_item + 1]) or (ONE_TEN[low_item] == ONE_TEN[low_item - 1]):
            return True
        low_item += 1       

    return False


def hasDuplicate(ONE_TEN:list) -> bool:
    '''This function tests if the list contains duplicates'''
    ONE_TEN.sort()
    
    for num in range(len(ONE_TEN)-1):

        if (ONE_TEN[num] == ONE_TEN[num + 1]):
            return True

    return False
 
        
if __name__=="__main__":
    main()

#case 1
#The original data for all functions is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#After swapping first and last:  [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
#After shifting right: [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#After replace even elements: [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
#After replacing with neighbors: [1, 3, 4, 5, 6, 7, 8, 9, 10, 10]
#After removing the middle element(s): [1, 2, 3, 4, 7, 8, 9, 10]
#After moving even elements: [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
#The second lagest value is: 9
#The list is in increasing order: True
#The list has adjacent duplicates: False
#The list has duplicates: False

#case 2
#The original data for all functions is: [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
#After swapping first and last:  [103, 20, 10, 14, 54, 16, 75, 38, 79, 12]
#After shifting right: [103, 12, 20, 10, 14, 54, 16, 75, 38, 79]
#After replace even elements: [0, 0, 0, 0, 0, 0, 75, 0, 79, 103]
#After replacing with neighbors: [12, 12, 14, 54, 54, 75, 75, 79, 103, 103]
#After removing the middle element(s): [12, 20, 10, 14, 75, 38, 79, 103]
#After moving even elements: [12, 20, 10, 14, 54, 16, 38, 75, 79, 103]
#The second lagest value is: 79
#The list is in increasing order: False
#The list has adjacent duplicates: False
#The list has duplicates: False

#case 3
#The original data for all functions is: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#After swapping first and last:  [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]
#After shifting right: [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#After replace even elements: [0, 9, 0, 7, 0, 5, 0, 3, 0, 1, 0]
#After replacing with neighbors: [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
#After removing the middle element(s): [10, 9, 8, 7, 6, 4, 3, 2, 1, 0]
#After moving even elements: [10, 8, 6, 4, 2, 0, 9, 7, 5, 3, 1]
#The second lagest value is: 9
#The list is in increasing order: False
#The list has adjacent duplicates: False
#The list has duplicates: False

#case 4
#The original data for all functions is: [10, 90, 8, 70, 6, 50, 6, 30, 2]
#After swapping first and last:  [2, 90, 8, 70, 6, 50, 6, 30, 10]
#After shifting right: [2, 10, 90, 8, 70, 6, 50, 6, 30]
#After replace even elements: [0, 0, 0, 0, 0, 0, 0, 0, 0]
#After replacing with neighbors: [10, 10, 70, 70, 70, 70, 70, 70, 2]
#After removing the middle element(s): [10, 90, 8, 70, 50, 6, 30, 2]
#After moving even elements: [10, 90, 8, 70, 50, 6, 6, 30, 2]
#The second lagest value is: 70
#The list is in increasing order: False
#The list has adjacent duplicates: False
#The list has duplicates: True

#case 5
#The original data for all functions is: [1, 3, 3, 15, 71, 9, 13, 5, 7, 9]
#After swapping first and last:  [9, 3, 3, 15, 71, 9, 13, 5, 7, 1]
#After shifting right: [9, 1, 3, 3, 15, 71, 13, 5, 7, 9]
#After replace even elements: [1, 3, 3, 15, 71, 9, 13, 5, 7, 9]
#After replacing with neighbors: [1, 3, 15, 71, 71, 71, 71, 71, 71, 9]
#After removing the middle element(s): [1, 3, 3, 15, 13, 5, 7, 9]
#After moving even elements: [1, 3, 3, 15, 71, 9, 13, 5, 7, 9]
#The second lagest value is: 15
#The list is in increasing order: False
#The list has adjacent duplicates: True
#The list has duplicates: True









































