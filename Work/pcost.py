# pcost.py
#
# Exercise 1.27

import sys

def portfolio_cost(filename):
    totalCost = 0.0
    with open(filename, 'rt') as file:
        headers = next(file)
        try:
            for line in file:
                shares = int(line.split(',')[1])
                price = float(line.split(',')[2])
                totalCost += shares*price
        except ValueError:
            print('Unable to parse a line')
    return totalCost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)

print(f'Total cost to buy all shares is {cost:.2f}')