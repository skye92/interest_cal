def account_balance():# def function/ what is function name, how many params.
    starting_balance = float(input("what is the starting balance? ")) # ask user for input for starting_balance

    stock_cost = float(input("how much does the stock cost? "))# ask user how much the stock cost

    stock_owned = starting_balance / stock_cost # how many of the stock is owned 

    dividend_amount = float(input("how much is the dividend")) #How much is the dividend 

    dividend_payment = stock_owned * dividend_amount # how much is the dividend payment 

    new_balance = starting_balance + dividend_payment # what is the new balance of the starting balance and the dividend payment 
    
    #print(new_balance) # print new balance 


    #create list that adds new_balance to it. 

    # define nested function 
    def interest_cal(new_balance):
        count = 0
        how_many = int(input("How many units of time? "))
        balance_list = [new_balance]

        while(count <= how_many):
            comp_interst = new_balance + dividend_payment # new balance + dividend payment is = to ? 
            count = count + 1

            for i in range(len(balance_list)):  
                i = balance_list.append(i + comp_interst)
            print(balance_list[-1])
# how many times to add the new balance to dividend payment 

# print results of new balance + dividend payment * how many times 
    interest_cal(new_balance)



account_balance()

