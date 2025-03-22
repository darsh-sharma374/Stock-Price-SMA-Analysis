import numpy as np

# Stock closing prices
stock_closing_prices = np.array([100, 102, 101, 105, 107, 110, 108, 115, 120, 125, 130, 128, 132, 135, 140])
window_size = 3

kernel = np.ones(window_size) / window_size
sma = np.convolve(stock_closing_prices, kernel, mode='valid')

buy_index = []
sell_index = []

# Loop through the SMA array
for i in range(1, len(sma)):
    if i + 1 < len(stock_closing_prices):
        if stock_closing_prices[i+1] > sma[i] and stock_closing_prices[i] <= sma[i-1]:
            buy_index.append(i+1)  # Record the day for the buy signal (i+1 because of valid mode)

        # Sell Signal Condition: Stock price crosses below the SMA
        elif stock_closing_prices[i+1] < sma[i] and stock_closing_prices[i] >= sma[i-1]:
            sell_index.append(i+1)  # Record the day for the sell signal (i+1)

# Print the results
print("Stock Closing Prices:", stock_closing_prices)
print("\n3-Day Simple Moving Average (SMA):")
print(np.round(sma, 2))  # Rounding to 2 decimal places for readability
print('**************************')
print("Buy Indices (days):", [day + 1 for day in buy_index])
print("Sell Indices (days):", [day + 1 for day in sell_index])
