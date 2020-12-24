
#Program to calculate and display the loan for buying a car


class Loan:

    #initializer
    def __init__(self, annualIntRate, numYearsLoan, loanAmnt, name):
        self.__annualIntRate = annualIntRate
        self.__numYearsLoan = numYearsLoan
        self.__loanAmnt = loanAmnt
        self.__name = name

    #getters   
    def getAnnualInterestRate(self):
        return self.__annualIntRate


    def getNumberYearsLoan(self):
        return self.__numYearsLoan


    def getLoanAmount(self):
        return self.__loanAmnt


    def getBorrowerName(self):
        return self.__name

    #setters
    def setAnnualInterestRate(self, annualIntRate):
        self.__annualIntRate = annualIntRate

    
    def setNumberYearsLoan(self, numYearsLoan):
        self.__numYearsLoan = numYearsLoan


    def setLoanAmount(self, loanAmnt):
        self.__loanAmnt = loanAmnt

    
    def setBorrowerName(self, name):
        self.__name = name

    #class methods
    def getMonthlyPayment(self):
        return self.__loanAmnt*(self.__annualIntRate/1200)/(1-(1/(1+(self.__annualIntRate/1200))**(self.__numYearsLoan*12)))


    def getTotalPayment(self):
        return self.getMonthlyPayment()*self.__numYearsLoan*12


def main():
    #ask input by the user
    annual_int = float(input("Enter yearly interest rate:"))
    #avoid division by 0
    while annual_int == 0:
        print("Rate cannot be 0")
        annual_int = float(input("Enter yearly interest rate:"))
        
    years = float(input("Enter number of years as an integer:"))
    
    while years == 0:
        print("number of years cannot be 0")
        years = float(input("Enter number of years as an integer:"))
    
    amount = float(input("Enter loan amount:"))
    borrower = input("Enter a borrower's name:")
    
    #create a loan
    loan1 = Loan(annual_int, years, amount, borrower)

    #output
    print("The loan is for", loan1.getBorrowerName())
    print("The monthly payment is", format(loan1.getMonthlyPayment(), ",.2f"))
    print("The total is", format(loan1.getTotalPayment(), ",.2f"))

    #ask for new calculation or finish the program
    again = input("\nDo you want to change the loan amount? Y for yes or enter to quit")

    while again == 'Y' or again == 'y':
        amount = float(input("Enter new loan amount:"))

        loan1 = Loan(annual_int, years, amount, borrower)
        print("The loan is for", loan1.getBorrowerName())
        print("The monthly payment is", format(loan1.getMonthlyPayment(), ",.2f"))
        print("The total is", format(loan1.getTotalPayment(), ",.2f"))

        again = input("\nDo you want to change the loan amount? Y for yes or enter to quit")
        

#call main function
if __name__=="__main__":
    main()


#case 1
#Enter yearly interest rate:2.5
#Enter number of years as an integer:5
#Enter loan amount:1000.00
#Enter a borrower's name:John Jones
#The loan is for John Jones
#The monthly payment is 17.75
#The total is 1,064.84
    
#Do you want to change the loan amount? Y for yes or enter to quity
#Enter new loan amount:5000
#The loan is for John Jones
#The monthly payment is 88.74
#The total is 5,324.21
    
#Do you want to change the loan amount? Y for yes or enter to quit


#case 2
#Enter yearly interest rate:5
#Enter number of years as an integer:10
#Enter loan amount:20000.00
#Enter a borrower's name:Anderson Silva
#The loan is for Anderson Silva
#The monthly payment is 212.13
#The total is 25,455.72

#Do you want to change the loan amount? Y for yes or enter to quit


#case 3
#Enter yearly interest rate:7.5
#Enter number of years as an integer:7
#Enter loan amount:10000.99
#Enter a borrower's name:Mike Tayson
#The loan is for Mike Tayson
#The monthly payment is 153.40
#The total is 12,885.43

#Do you want to change the loan amount? Y for yes or enter to quitY
#Enter new loan amount:99999.99
#The loan is for Mike Tayson
#The monthly payment is 1,533.83
#The total is 128,841.50

#Do you want to change the loan amount? Y for yes or enter to quity
#Enter new loan amount:10000
#The loan is for Mike Tayson
#The monthly payment is 153.38
#The total is 12,884.15

#Do you want to change the loan amount? Y for yes or enter to quitn


#case 4
#Enter yearly interest rate:1
#Enter number of years as an integer:1
#Enter loan amount:11111.11
#Enter a borrower's name:Minotauro
#The loan is for Minotauro
#The monthly payment is 930.95
#The total is 11,171.39

#Do you want to change the loan amount? Y for yes or enter to quity
#Enter new loan amount:10000
#The loan is for Minotauro
#The monthly payment is 837.85
#The total is 10,054.25

#Do you want to change the loan amount? Y for yes or enter to quit


#case 5
#Enter yearly interest rate:0
#Rate cannot be 0
#Enter yearly interest rate:0
#Rate cannot be 0
#Enter yearly interest rate:1
#Enter number of years as an integer:0
#number of years cannot be 0
#Enter number of years as an integer:0
#number of years cannot be 0
#Enter number of years as an integer:2
#Enter loan amount:0
#Enter a borrower's name:
#The loan is for 
#The monthly payment is 0.00
#The total is 0.00

#Do you want to change the loan amount? Y for yes or enter to quity
#Enter new loan amount:1000
#The loan is for 
#The monthly payment is 42.10
#The total is 1,010.45

#Do you want to change the loan amount? Y for yes or enter to quit
