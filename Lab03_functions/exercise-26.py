
#This program write the first letters of the full name.

def load() -> (str):
    '''ask for the user input the full name'''
    full_name = input('Enter your full name: ')
    return full_name


def get_names(full_name:str) -> None:
    '''get full name entered and print the initials'''
    #split the full name
    names = full_name.split()
    #define the initial letter for each word 
    for initial in names:
        #output
        print(initial[:1].upper(), end = '.')

   
def main():
    #call the functions
    full_name = load()
    get_names(full_name)
    

if __name__=="__main__":
    main()

# case 1
# Enter your full name: James Tiberias Kirk
# J.T.K.

# case 2
# Enter your full name: rodrigo carvalhaes silva
# R.C.S.

# case 3
# Enter your full name: George W. Bush
# G.W.B.

# case 4
# Enter your full name: tony Stark
# T.S.

# case 5
# Enter your full name: Pedro de Alcântara Francisco António João Carlos Xavier de Paula Miguel Rafael Joaquim José Gonzaga Pascoal Cipriano Serafim
# P.D.A.F.A.J.C.X.D.P.M.R.J.J.G.P.C.S.