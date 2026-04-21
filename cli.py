from orders import check_price

def main():
    print("=== Trading Bot ===")

    symbol = input("Enter symbol (BTCUSDT): ").upper()

    if symbol != "BTCUSDT":
        print("Only BTCUSDT supported for now ❌")
        return

    runs = input("How many times to run bot: ")

    if not runs.isdigit():
        print("Invalid number ❌")
        return

    runs = int(runs)

    for i in range(runs):
        price = check_price()
        print(f"Current Price: {price}")
        print("-" * 30)


if __name__ == "__main__":
    main()