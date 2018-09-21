def mortgage_calc (Principal,month_payment,interest_rate):
    import pandas as pd
    import numpy as np
    #Principal = 100000
    #month_payment = 500   
    #interest_rate = .05

    if interest_rate >= 1.0:
        interest_rate = interest_rate / 100

    if interest_rate < 0:
        print("interest rate should be a positive number")

    # n = Total number of months until payment is 0. 
    # This is a formula we used during our finance class.
    # Good documentation is here: http://www.seanerikoconnor.freeservers.com/MortgageLoanDerivation.pdf
    #
    # In short I needed to find a way to fill empty arrays with a specific length (n). This will tell us how large our
    #   for loop should be
    monthly_interest_rate = interest_rate / 12
    numerator = np.log(1- monthly_interest_rate * Principal /month_payment) * -1
    denominator = np.log(1+ monthly_interest_rate)
    n = int(numerator / denominator)

    # EMPTY LISTS HERE #
    col_Month = [0]*int(n+2)                       # Month
    col_Payment = [month_payment]*int(n+2)         # Monthly Payment
    col_interest = [0]*int(n+2)                    # Interest Payment
    col_balance = [0]*int(n+2)                     # Balance left after every month. This is key!

    for i in range(0,n+1):
    #for i in range(1,10):
        col_Month[i] = i +1

        if i==0:
            Interest_payment = Principal * (interest_rate / 12)
            col_interest[i] = Interest_payment
            bal = (Principal + Interest_payment) - month_payment
            col_balance[i] = bal
        
        # THIS WILL TEST TO SEE IF WE WILL GO NEGATIVE ON BALANCE. 
        # In other words, for the last month in our array we are going to calculate a new payment method s.t.
        # NEW PAYMENT = previous balance - interest  
        # 
        # BUT ONLY FOR THE MONTH WHERE THE CONDITION IS MET. (i.e. previous months balance < 500 = month_ payment)
        else:
            if col_balance[(i-1)] <= col_Payment[(i-1)]:
                Interest_payment = col_balance[(i-1)] * (interest_rate / 12)
                col_interest[i] = Interest_payment

                col_Payment[i] = col_balance[(i-1)] + col_interest[i]
                col_balance[i] = (col_balance[(i-1)] + col_interest[i]) -  col_Payment[i]  

            else:
                Interest_payment = col_balance[(i-1)] * (interest_rate / 12)
                col_interest[i] = Interest_payment
                new_bal = (col_balance[(i-1)] + Interest_payment) - month_payment
                col_balance[i] =  new_bal  # This is where we can fill our new array. 
    for i in range(0,(int(n+2))):
        if col_balance[i]<= 0:
            print(i)
            max_i = int(i)
            break
    
    new_col_Month = col_Month[0:(max_i+1)]
    new_col_Payment = col_Payment[0:(max_i+1)]
    new_col_interest = col_interest[0:(max_i+1)]
    new_col_balance = col_balance[0:(max_i+1)]
    
    #round(col_balance,ndigits=2)
    data = {'Month':new_col_Month,
            'Payment':new_col_Payment,
            'Interest': new_col_interest,
            'Balance':new_col_balance}

    ARRAY = pd.DataFrame(data)
    print('It will take',max(col_Month),' Months to pay off the Mortgage')
    print(' ')
    print('The total amount paid =',round(sum(new_col_Payment) + sum(new_col_interest),ndigits=2))
    print(' ')
    return(ARRAY)


result = mortgage_calc (100000,500,.05)
print(result)
