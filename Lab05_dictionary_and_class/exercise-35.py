
#Program translate to English the
#abbreviations entered by the user.


def main():

    #call functions
    abrv_dict = create_dictionary()
    mssg = get_message()
    translate_text(abrv_dict, mssg)
    

def create_dictionary()->dict:
    '''Function creates a dictionary by a text file'''
    infile = open('textabbv.txt', 'r')
    abbv_dict = {}

    line = infile.readline()
    while line != '':
        line = line.rstrip('\n')
        line = line.split(':', 1)
        abbv_dict[line[0]] = line[1]
        line = infile.readline()

    return abbv_dict


def get_message()->str:
    '''Function asks to user enter the input,
    text with abbreviations'''
    mssg = input("Enter a message to be translated:\n")

    return mssg


def translate_text(abrv_dict:dict, mssg:str)->None:
    '''Function compare if the dictionary contains the
    abbreviations and translate it'''
    words = mssg.split() 
    text = ''
    
    for abrv in words:
        lastChar  = abrv[-1]
        if lastChar in ".?!,;:":
            abrv = abrv.rstrip(lastChar)
        else:
            lastChar = ''
            
        if abrv in abrv_dict:
            abrv = abrv_dict[abrv]
            text = text + abrv + lastChar + ' '
        else:
            text = text + abrv + lastChar + ' '

    print("The translated text is:")
    print(text)
   

if __name__=="__main__":
    main()


#case 1
#Enter a message to be translated:
#r u, lol?
#The translated text is:
#are you, laughing out loud?


#case 2
#Enter a message to be translated:
#hi bff, ttyl
#The translated text is:
#hi best friend forever, talk to you later


#case 3
#Enter a message to be translated:
#tldr, nw sry :(
#The translated text is:
#too long; didn't read, no way! sorry :(


#case 4
#Enter a message to be translated:
#I Don't use abbreviations
#The translated text is:
#I Don't use abbreviations


#case 5
#Enter a message to be translated:
#rofl! omg! rus sry, r u jk? right?
#The translated text is:
#rolling on floor laughing! oh my gosh! are you serious? sorry, are you just kidding? right? 
