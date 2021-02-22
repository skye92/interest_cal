starting = float(input("what is the starting balance? "))


def interest_cal(starting_balance):
    # starting = int(input("what is the starting balance? "))
    starting_balance = [starting, ]
    cost_per_share = int(input("How much does the stock cost? "))
    initial_stock_amount = starting_balance[-1] / cost_per_share
    stock_amount_list = [initial_stock_amount, ]
    dividend = float(input("How much is the dividend? "))

    how_many_times = int(input("How many units of time? "))
    times = 0

    while(times <= how_many_times):
        dividend_payment = stock_amount_list[-1] * dividend
        result = dividend_payment + starting_balance[-1]
        stock_amount = result / cost_per_share
        starting_balance.append(result)
        stock_amount_list.append(stock_amount)
        times = times + 1
        print(f"Your dividend per time unit is {dividend_payment} ")
        print(starting_balance[-1])


interest_cal(starting)
