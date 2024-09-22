import yfinance as yf

def get_stock_information(stock):
    print(stock.info)
    # get historical market data
    hist = stock.history(period="1mo")

    # show meta information about the history (requires history() to be called first)
    print(stock.history_metadata)

    # show actions (dividends, splits, capital gains)
    print(stock.actions)
    print(stock.dividends)
    print(stock.splits)
    print(stock.capital_gains)


    # show financials:
    print(stock.calendar)
    print(stock.sec_filings)
    # - income statement
    print(stock.income_stmt)
    print(stock.quarterly_income_stmt)
    # - balance sheet
    print(stock.balance_sheet)
    print(stock.quarterly_balance_sheet)
    # - cash flow statement
    print(stock.cashflow)
    print(stock.quarterly_cashflow)
    # see `Ticker.get_income_stmt()` for more options

    # show holders
    print(stock.major_holders)
    print(stock.institutional_holders)
    print(stock.mutualfund_holders)
    print(stock.insider_transactions)
    print(stock.insider_purchases)
    print(stock.insider_roster_holders)

    # show recommendations
    print(stock.recommendations)
    print(stock.recommendations_summary)
    print(stock.upgrades_downgrades)

    # show analysts data
    print(stock.analyst_price_targets)
    print(stock.earnings_estimate)
    print(stock.revenue_estimate)
    print(stock.earnings_history)
    print(stock.eps_trend)
    print(stock.eps_revisions)
    print(stock.growth_estimates)

    print(stock.earnings_dates)

    # show ISIN code - *experimental*
    # ISIN = International Securities Identification Number
    print(stock.isin)

    # show options expirations
    print(stock.options)

# show news
stock1 = yf.Ticker("MSFT")
news = stock1.news
for new in news:
    print(new['title'])