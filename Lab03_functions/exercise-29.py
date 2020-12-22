
#Program shows if the word is a palindrome or not


def isPalindrome(word:str) -> None:
    '''define if word is a palindrome or not'''
    word = word.lower()
    reverse = ""
    
    #loop to revert to word
    for charac in word:
        reverse = charac + reverse

    #output
    if (reverse == word):
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")

    
def main():
    countWords = int(input("How many words do you want to check? "))
    
    #define how many words you want to test
    for words in range(countWords):
        print()
        word = input("Enter a String: ")
        isPalindrome(word)
    
          
if __name__=="__main__":
    main()


# case 1
# How many words do you want to check? 4

# Enter a String: noon
# noon is a palindrome

# Enter a String: print
# print is not a palindrome

# Enter a String: racecar
# racecar is a palindrome

# Enter a String: speed
# speed is not a palindrome

# case 2
# How many words do you want to check? 3

# Enter a String: Dad
# dad is a palindrome

# Enter a String: dead
# dead is not a palindrome

# Enter a String: did
# did is a palindrome

# case 3
# How many words do you want to check? 3

# Enter a String: Mom
# mom is a palindrome

# Enter a String: man
# man is not a palindrome

# Enter a String: main
# main is not a palindrome

# case 4
# How many words do you want to check? 0
# >>> 

# case 5
# How many words do you want to check? 3

# Enter a String: arara
# arara is a palindrome

# Enter a String: Hannah
# hannah is a palindrome

# Enter a String: rotator
# rotator is a palindrome