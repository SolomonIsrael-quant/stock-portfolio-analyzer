import numpy as np

stocks = np.array([[100, 78, 90, 108, 110, 105, 107, 99, 95,110],
                  [120, 115, 110, 120, 130, 135, 110, 105, 103, 120],
                  [102, 103, 105, 100, 109, 110, 111, 107, 106,111]])

stock_name = ['ALPHA', 'BETA', 'GAMMA']

daily_return = np.diff(stocks, axis=1)

for i in range(len(stocks)):
    stock = stocks[i]
    stock_returns = daily_return[i]
    print(f'======{stock_name[i]}======')

    print(f'Average Price: {np.mean(stock)}')
    print(f'Highest Price: {np.max(stock)}')
    print(f'Lowest Price: {np.min(stock)}')
    print(f'Volatility (std): {np.std(stock)}')

    print(f'Up Days: {np.sum(stock_returns > 0)}')
    print(f'Down Days: {np.sum(stock_returns < 0)}')

    print()
    print()

print(f'Correlation ALPHA and BETA {np.corrcoef(stocks[0], stocks[1])[0][1]}')
print(f'Correlation ALPHA and GAMMA {np.corrcoef(stocks[0], stocks[2])[0][1]}')

for i in range(len(stocks)):
    p75 = np.percentile(stocks[i], 75)
    current = stocks[i][-1]
    if current > p75:
        print(f'{stock_name[i]}: SELL SIGNAL')
    else:
        print(f'{stock_name[i]}: BUY SIGNAL')

avg = np.mean(stocks, axis=1)
best = stock_name[np.argmax(avg)]
print(f'Best stock by average price: {best}')