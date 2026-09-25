# CMPE 285 Homework 4

A Python stock profit calculator that reports proceeds, total cost, net profit, return on investment, and break-even share price.

## Setup and run

1. Install Python 3 from https://www.python.org/downloads/ if needed. On Windows, enable the installer option to add Python to PATH if offered.
2. Save `stock_profit_calculator.py` in a folder on your computer.
3. Open a terminal in that folder. On macOS/Linux, check the installation with `python3 --version`, then run:

   ```sh
   python3 stock_profit_calculator.py
   ```

   On Windows, use `py --version` and:

   ```sh
   py stock_profit_calculator.py
   ```

   Alternatively, open the file in Python's IDLE editor and select **Run > Run Module** (F5).
4. Answer all seven prompts. Enter `20` for a 20% tax rate. Prices and commissions are dollar amounts; each commission is the total fee for its transaction.

Only Python's standard library is used. No packages or API keys are required. The stock symbol labels the report; the program uses the prices you enter and does not download market prices.

## Research and formulas

The IRS explains that stock purchase basis generally includes the purchase price and purchase commissions. Selling expenses also affect the gain calculated on a sale. Sources:

- IRS, capital gains and losses FAQ: https://www.irs.gov/faqs/capital-gains-losses-and-sale-of-home
- IRS, Publication 550 (Investment Income and Expenses): https://www.irs.gov/publications/p550

This assignment uses a simplified model: one purchase, one sale, fixed commissions, and a user-supplied tax rate. Tax is charged only on a positive gain; losses do not produce a tax credit in this program.

Let N be shares, F the final price, I the initial price, B the buy commission, S the sell commission, and r the tax percentage divided by 100.

| Quantity | Formula |
| --- | --- |
| Proceeds | N × F |
| Cost before tax | N × I + B + S |
| Capital gain before tax | Proceeds − cost before tax |
| Tax on capital gain | max(capital gain, 0) × r |
| Cost | Cost before tax + tax |
| Net profit | Proceeds − cost |
| Return on investment (%) | Net profit ÷ cost × 100 |
| Break-even share price | Cost before tax ÷ N |

The ROI formula uses total cost, including tax, as the denominator. This matches the instructor's ADBE example (189.76%).

At break-even, sale proceeds cover the share purchase and both commissions. There is no capital gain, so the tax is zero. Therefore, the tax from a different, profitable sale should not be included in the break-even price. The displayed break-even value is rounded to two decimal places; the underlying calculation is not rounded early.

The program accepts positive whole-number share counts, nonnegative prices and commissions, and a tax rate from 0 to 100. It rejects invalid numeric input. ROI is reported as N/A if total cost is zero. Money is displayed to two decimal places.

## Example

These are hypothetical prices, not a current stock quote.

| Input | Value |
| --- | --- |
| Stock symbol | AAPL |
| Allotment | 100 |
| Final share price | 60 |
| Sell commission | 10 |
| Initial share price | 50 |
| Buy commission | 10 |
| Capital gain tax rate | 20 |

Proceeds = 100 × 60 = $6,000.00.

Cost before tax = 100 × 50 + 10 + 10 = $5,020.00.

Capital gain = 6,000 − 5,020 = $980.00.

Tax = 980 × 0.20 = $196.00.

Cost = 5,020 + 196 = $5,216.00.

Net profit = 6,000 − 5,216 = $784.00.

ROI = 784 ÷ 5,216 × 100 = 15.03%.

Break-even price = 5,020 ÷ 100 = $50.20 per share.

## How to submit

Email the program source code and run script to learnbeetle@gmail.com before the beginning of your next class.

The prepared `stock_profit_homework.zip` contains:

- `stock_profit_calculator.py`: the program source code.
- `run.sh`: the run script for macOS/Linux. Extract the ZIP, open a terminal in the extracted folder, and enter `bash run.sh`. On Windows, run the Python source directly with `py stock_profit_calculator.py`.
- `sample_run.txt`: the inputs and actual output for the instructor's ADBE example.
- `README.md`: setup instructions and formula explanations.

The phrase "run script" may mean a launcher script or a record of program execution, so both are included.

1. Review the code and run it yourself.
2. Compose an email to learnbeetle@gmail.com with subject `Stock Profit Calculator Homework - [Your Name] - [Course/Section]`.
3. Attach the ZIP, or attach the source, run script, and sample output individually if your instructor prefers separate files.
4. Replace the name and course placeholders with your own details, send before the deadline, and verify that the email appears in Sent.

Do not submit only a screenshot. Review and understand the code, and follow your course's policy on outside or AI assistance.
