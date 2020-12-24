
#This program asks to the user how many years
#studying and it shows the student rank name 

def main():
    #ask to user how many years studying
    print("Enter the numbers of years studying: ", end="")
    years = input("(1, 2, 3 or 4):")
    #output calling the function
    print("You are", determineRank(years))


def determineRank(years:dict) ->dict:
    '''This function defines the student rank name and returns
    the user choice'''
    #loop to avoid error type
    while int(years) < 1 or int(years) > 4:
        print("Enter the numbers of years studying: ", end="")
        years = input("(1, 2, 3 or 4):")
        
    #define dictionary
    dict = {'1':"Freshman", '2':"Sophomore", '3':"Junior", '4':"Senior"}
    #return value
    return dict[years]


#call the main function
if __name__=="__main__":
    main()
    

# case 1
# Enter the numbers of years studying: (1, 2, 3 or 4):1
# You are Freshman

# case 2
# Enter the numbers of years studying: (1, 2, 3 or 4):2
# You are Sophomore

# case 3
# Enter the numbers of years studying: (1, 2, 3 or 4):3
# You are Junior

# case 4
# Enter the numbers of years studying: (1, 2, 3 or 4):4
# You are Senior

# case 5
#Enter the numbers of years studying: (1, 2, 3 or 4):0
#Enter the numbers of years studying: (1, 2, 3 or 4):5
#Enter the numbers of years studying: (1, 2, 3 or 4):-1
#Enter the numbers of years studying: (1, 2, 3 or 4):99
#Enter the numbers of years studying: (1, 2, 3 or 4):2
#You are Sophomore
