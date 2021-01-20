def interest_cal():
    user_list = []

    user_input = float(input("please enter a starting amount"))

    user_list.append(user_input)

    starting_balance = user_list

    # starting_balance = input("how much is the starting balance?")

    new_monthly_balance = 0

    my_balance = (starting_balance) + (new_monthly_balance)

    cost_of_share = input("how much does the stock cost?")

    shares_owned = float(cost_of_share) / my_balance

    dividend_payout = input("how much is the monthly divided payment?")

    interest = shares_owned * float(dividend_payout)

    new_monthly_balance = shares_owned + interest

    return(new_monthly_balance)

interst_call_results = interest_cal()

count= 0

how_many = int(input("how many units of time?"))

while(count <= int(how_many)):
        print(interst_call_results)
        count = count + 1