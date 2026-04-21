from client import get_price

prices = []
balance = 1000
position = 0
entry_price = 0

def moving_average(data, period):
    if len(data) < period:
        return None
    return sum(data[-period:]) / period


def check_price():
    global balance, position, entry_price

    price = get_price()
    prices.append(price)

    short_ma = moving_average(prices, 3)
    long_ma = moving_average(prices, 5)

    print(f"Price: {price}")

    # BUY condition
    if short_ma and long_ma and short_ma > long_ma and balance > 0:
        position = balance / price
        entry_price = price
        balance = 0
        print("BUY executed ✅")

    # SELL condition (trend)
    elif short_ma and long_ma and short_ma < long_ma and position > 0:
        balance = position * price
        position = 0
        print("SELL (trend) 🚨")

    # STOP-LOSS (very important)
    elif position > 0 and price < entry_price * 0.98:
        balance = position * price
        position = 0
        print("STOP-LOSS triggered ❌")

    # PROFIT tracking
    total_value = balance + (position * price)
    profit = total_value - 1000

    print(f"Balance: {balance}")
    print(f"Position: {position}")
    print(f"Total Value: {total_value}")
    print(f"Profit: {profit}")
    print("-" * 30)

    return price