starting = int(input("what is the starting balance? "))

def interest_cal(starting_balance):
    # starting = int(input("what is the starting balance? "))
    starting_balance = [starting,]
    cost_per_share = int(input("How much does the stock cost? "))
    stock_amount = starting_balance[0] / cost_per_share
    dividend = float(input("How much is the dividend? "))
    dividend_payment = stock_amount * dividend

    how_many_times = int(input("How many units of time? "))
    times = 0

    while(times <= how_many_times):
        result = dividend_payment + starting_balance[-1]
        starting_balance.append(result)
        times = times +1
        print(starting_balance[-1])


interest_cal(starting)

