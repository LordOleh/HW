import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

data = yf.download("NVDA", period="10y")
df = pd.DataFrame(data)
print(df.tail(100))

data["MA_100"] = data['Close'].rolling(100).mean()
data["MA_20"] = data['Close'].rolling(20).mean()
data.loc[data["MA_20"] > data["MA_100"], "Signal"] = "Buy"
data.loc[data["MA_20"] < data["MA_100"], "Signal"] = "Sell"

data[['Close', 'MA_20', 'MA_100']].plot(figsize=(14, 7))
plt.xlabel('Date')
plt.ylabel('$')
plt.show()

q = 5
profit = 0
status = False
my_trades = []

for i in range(1, len(data)):
    prev_signal = data['Signal'].iloc[i-1]
    curr_signal = data['Signal'].iloc[i]
    curr_price = float(data['Close'].iloc[i])
    curr_date = data.index[i]

    if curr_signal == 'Buy' and prev_signal == 'Sell' and status == False:
        profit += (-q)*curr_price
        status = True
        my_trades.append([curr_date, curr_price, curr_signal, profit])
    elif curr_signal == 'Sell' and prev_signal == 'Buy' and status == True:
        profit += q*curr_price
        status = False
        my_trades.append([curr_date, curr_price, curr_signal, profit])

if status == True:
    last_price = data['Close'].iloc[-1]
    last_date = data.index[-1]
    profit += q*last_price
    status = False
    my_trades.append([last_date, last_price, "Sell", profit])

trades_df = pd.DataFrame(my_trades, columns=["Date", "Price", "Action", "Profit"])
print(trades_df.head())

print(f"\nЗагальний прибуток: {profit} $")
