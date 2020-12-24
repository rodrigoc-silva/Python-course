
#Program calculates the sum of tea sales and
#print out the sales by tea type and store.

def main():

    tea_file = open('tea.txt', 'r')

    tea_dict = {}

    #read lines of the file
    line = tea_file.readline()
    while line != '':
        line = line.rstrip('\n')
        line = line.split(':', 1)
        tea_dict[line[0]] = line[1]
        line = tea_file.readline()
        
    #define variables
    sum_store1 = sum_store2 = sum_store3 = 0
    value = ''

    #loop to read each key and value in the dictionary
    for key in sorted(tea_dict):

        value = tea_dict[key].split(':', 2)
        store1_sales = float(value[0])
        store2_sales = float(value[1])
        store3_sales = float(value[2])
        
        #calculate the sum of each tea type and each store
        sum_tea = store1_sales + store2_sales + store3_sales
        sum_store1 += store1_sales
        sum_store2 += store2_sales
        sum_store3 += store3_sales

        #output key, values and tea sum
        print('%-9s %10.2f %10.2f %10.2f %10.2f' % (key, store1_sales, store2_sales, store3_sales, sum_tea))
 
    #output the store sum   
    print('%-9s %10.2f %10.2f %10.2f' % ('', sum_store1, sum_store2, sum_store3))
       
    tea_file.close()


if __name__=="__main__":
    main()


#case 1
#Ceylon       6700.10    5012.45    6011.00   17723.55
#Earl Grey   10225.25    9025.00    9505.00   28755.25
#Green Tea    8580.00    7201.25    8900.00   24681.25
#Jasmine      9285.15    8276.10    8705.00   26266.25
#Mint Tea     7901.25    4267.00    7056.50   19224.75
#            42691.75   33781.80   40177.50

#case 2
#Black Tea       0.00       0.00       0.00       0.00
#Ceylon       6700.10    5012.45    6011.00   17723.55
#Earl Grey   10225.25    9025.00    9505.00   28755.25
#Green Tea    8580.00    7201.25    8900.00   24681.25
#Jasmine      9285.15    8276.10    8705.00   26266.25
#Mint Tea     7901.25    4267.00    7056.50   19224.75
#            42691.75   33781.80   40177.50


#case 3
#Ceylon       6700.10    5012.45       0.00   11712.55
#Earl Grey   10225.25    9025.00       0.00   19250.25
#Green Tea    8580.00    7201.25       0.00   15781.25
#Jasmine      9285.15    8276.10       0.00   17561.25
#Mint Tea     7901.25    4267.00       0.00   12168.25
#            42691.75   33781.80       0.00


#case 4
#Ceylon          0.00       0.00       0.00       0.00
#Earl Grey   10225.25    9025.00    9505.00   28755.25
#Green Tea    8580.00    7201.25    8900.00   24681.25
#Jasmine      9285.15    8276.10    8705.00   26266.25
#Mint Tea     7901.25    4267.00    7056.50   19224.75
#            35991.65   28769.35   34166.50


#case 5
#Ceylon       6700.10    5012.45    6011.00   17723.55
#Earl Grey   10225.25    9025.00    9505.00   28755.25
#Green Tea    8580.00    7201.25    8900.00   24681.25
#Mint Tea     7901.25    4267.00    7056.50   19224.75
#            33406.60   25505.70   31472.50
