"""Stock profit calculator. Run with: python3 stock_profit_calculator.py"""

import math


def read_number(prompt, minimum=0, maximum=None):
    """Keep asking until the user enters a finite number in the allowed range."""
    while True:
        try:
            value = float(input(prompt))
            if not math.isfinite(value) or value < minimum:
                raise ValueError
            if maximum is not None and value > maximum:
                raise ValueError
            return value
        except ValueError:
            if maximum is None:
                print(f"Please enter a number greater than or equal to {minimum}.")
            else:
                print(f"Please enter a number from {minimum} to {maximum}.")


def read_allotment():
    """The number of shares must be a positive whole number."""
    while True:
        try:
            shares = int(input("Allotment (number of shares): "))
            if shares > 0:
                return shares
        except ValueError:
            pass
        print("Please enter a positive whole number, such as 100.")


def calculate_profit(shares, final_price, sell_commission, initial_price,
                     buy_commission, tax_rate):
    """Calculate results; tax_rate is a percentage, such as 20 for 20%."""
    proceeds = shares * final_price
    purchase_cost = shares * initial_price
    cost_before_tax = purchase_cost + buy_commission + sell_commission
    capital_gain = proceeds - cost_before_tax

    # This homework model does not give a tax credit for a loss.
    tax = max(capital_gain, 0) * (tax_rate / 100)
    cost = cost_before_tax + tax
    net_profit = proceeds - cost

    # Use the assignment's total cost as the ROI denominator.
    roi = (net_profit / cost) * 100 if cost > 0 else None

    # At break-even, capital gain and its tax are both zero.
    break_even_price = cost_before_tax / shares

    return {
        "proceeds": proceeds,
        "tax": tax,
        "cost": cost,
        "net_profit": net_profit,
        "roi": roi,
        "break_even_price": break_even_price,
    }


def main():
    print("Stock Profit Calculator")
    print("Enter numbers without dollar signs, commas, or percent signs.\n")

    symbol = input("Stock symbol: ").strip().upper()
    while not symbol:
        symbol = input("Please enter a stock symbol: ").strip().upper()

    shares = read_allotment()
    final_price = read_number("Final share price ($): ")
    sell_commission = read_number("Sell commission ($): ")
    initial_price = read_number("Initial share price ($): ")
    buy_commission = read_number("Buy commission ($): ")
    tax_rate = read_number("Capital gain tax rate (%): ", maximum=100)

    results = calculate_profit(shares, final_price, sell_commission,
                               initial_price, buy_commission, tax_rate)

    print(f"\nStock Profit Report: {symbol}")
    print(f"Proceeds: ${results['proceeds']:,.2f}")
    print(f"Cost: ${results['cost']:,.2f}")
    print(f"Net Profit: ${results['net_profit']:,.2f}")
    if results["roi"] is None:
        print("Return on investment: N/A (total cost is zero)")
    else:
        print(f"Return on investment: {results['roi']:.2f}%")
    print(f"Break even price: ${results['break_even_price']:,.2f}")


if __name__ == "__main__":
    main()
