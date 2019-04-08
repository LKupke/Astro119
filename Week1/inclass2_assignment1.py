#python 3.7.2
"""
Alternate Name: Annual Savings
*compute annual dollar amount on savings invested at 10% over i_Years years variables:
**i_Years = duration of investment
**f_interest = interest ragte
**f_iniInvest= initial investment

output
savings in last year (i_Years)
"""

import numpy as np

#define variables
i_Years     = 30
f_interest  = 0.1
f_iniInvest = 1e4

#Computation
def annual_return(f_iniInvest,f_interest,i_Years):
    currInvest=f_iniInvest
    for i in range(i_Years):
        fGrowth=currInvest*f_interest
        #print('Year',i+1,'savings',round(currInvest,2))
        currInvest += fGrowth
    return currInvest
print(annual_return(f_iniInvest,f_interest,i_Years))
