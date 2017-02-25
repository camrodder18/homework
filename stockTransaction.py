#Stock Transaction Program - Page 79 (40 points)
#Submit a file called stock.py
#Make sure the money output is formatted to 2 decimal places and uses a comma where needed.
#Your program must perform all calculations and store the results in variables.

shares = 2000
stock_price = float(40)
final_price = float(42.75)
value1 = shares * stock_price
value2 = shares * final_price
commission1 = value1 * .03
commission2 = value2 * .03


print('Joe paid $', format(value1, ',.2f'), 'dollars for the stocks.')
print('Joe paid his broker $',format(commission1, ',.2f'), 'dollars for initial commission')
print('Joe sold his stocks for $', format(value2, ',.2f') , 'dollars')
print('Joe paid his broker $', format(commission2, ',.2f'), 'dollars for final commission')
print('Joe has $', format(value2 - (commission1 + commission2),',.2f'),'dollars remaining')








