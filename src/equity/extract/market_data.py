import yfinance as yf
import duckdb
import pandas as pd


def create_table_insert_data(table_name, df):
    with duckdb.connect("../../../db/equities.db") as con:
        try:
            con.sql("CREATE TABLE " + table_name + " AS SELECT * FROM df")
        except:
            pass
        try:
            con.sql("INSERT INTO " + table_name + " SELECT * FROM df")
        except:
            pass

def get_dataframe(symbol, obj):
    try:
        if isinstance(obj, dict):
            df = pd.DataFrame([obj])
        elif isinstance(obj, list):
            df = pd.DataFrame(obj)
        else:
            df = obj
        df = df.reset_index()
        df['Symbol'] = symbol
        return df
    except Exception as e:
        print(obj)
        raise e

def get_equities_market_data(stock):
    print("get historical market data")
    df = get_dataframe(stock.ticker, stock.history(period="5y"))
    create_table_insert_data("historical_market_data", df)
    print("get meta data")
    df = get_dataframe(stock.ticker, stock.history_metadata)
    create_table_insert_data("historical_meta_data", df)
    print("get calendar data")
    df = get_dataframe(stock.ticker, stock.calendar)
    create_table_insert_data("calendar", df)
    print("get sec filing")
    df = get_dataframe(stock.ticker, stock.sec_filings)
    create_table_insert_data("sec_filings", df)
    print("get income stmt")
    df = get_dataframe(stock.ticker, stock.income_stmt)
    create_table_insert_data("income_stmt", df)
    print("get quarterly income stmt")
    df = get_dataframe(stock.ticker, stock.quarterly_income_stmt)
    create_table_insert_data("quarterly_income_stmt", df)
    print("get balance sheet")
    df = get_dataframe(stock.ticker, stock.balance_sheet)
    create_table_insert_data("balance_sheet", df)
    print("get quarterly balance sheet")
    df = get_dataframe(stock.ticker, stock.quarterly_balance_sheet)
    create_table_insert_data("quarterly_balance_sheet", df)
    print("get cashflow")
    df = get_dataframe(stock.ticker, stock.cashflow)
    create_table_insert_data("cashflow", df)
    print("get quarterly cashflow")
    df = get_dataframe(stock.ticker, stock.quarterly_cashflow)
    create_table_insert_data("quarterly_cashflow", df)
    print("get major holders")
    df = get_dataframe(stock.ticker, stock.major_holders)
    create_table_insert_data("major_holders", df)
    print("get institutional holders")
    df = get_dataframe(stock.ticker, stock.institutional_holders)
    create_table_insert_data("institutional_holders", df)
    print("get mutual fund holders")
    df = get_dataframe(stock.ticker, stock.mutualfund_holders)
    create_table_insert_data("mutualfund_holders", df)
    print("get insider transactions")
    df = get_dataframe(stock.ticker, stock.insider_transactions)
    create_table_insert_data("insider_transactions", df)
    print("get insider purchases")
    df = get_dataframe(stock.ticker, stock.insider_purchases)
    create_table_insert_data("insider_purchases", df)
    print("get insider roster holders")
    df = get_dataframe(stock.ticker, stock.insider_roster_holders)
    create_table_insert_data("insider_roster_holders", df)
    print("get recommendations")
    df = get_dataframe(stock.ticker, stock.recommendations)
    create_table_insert_data("recommendations", df)
    print("get upgrades_downgrades")
    df = get_dataframe(stock.ticker, stock.upgrades_downgrades)
    create_table_insert_data("upgrades_downgrades", df)
    print("get analyst price targets")
    df = get_dataframe(stock.ticker, stock.analyst_price_targets)
    create_table_insert_data("analyst_price_targets", df)
    print("get earnings estimate")
    df = get_dataframe(stock.ticker, stock.earnings_estimate)
    create_table_insert_data("earnings_estimate", df)
    print("get revenue estimate")
    df = get_dataframe(stock.ticker, stock.revenue_estimate)
    create_table_insert_data("revenue_estimate", df)
    print("get earnings history")
    df = get_dataframe(stock.ticker, stock.earnings_history)
    create_table_insert_data("earnings_history", df)
    print("get eps trend")
    df = get_dataframe(stock.ticker, stock.eps_trend)
    create_table_insert_data("eps_trend", df)
    print("get eps revisions")
    df = get_dataframe(stock.ticker, stock.eps_revisions)
    create_table_insert_data("eps_revisions", df)
    print("get growth estimates")
    df = get_dataframe(stock.ticker, stock.growth_estimates)
    create_table_insert_data("growth_estimates", df)
    print("get earnings dates")
    df = get_dataframe(stock.ticker, stock.earnings_dates)
    create_table_insert_data("earnings_dates", df)


with duckdb.connect("../../../db/equities.db") as con:
    # Run a query to get data from the table
    result = con.execute("select distinct(symbol) from companies WHERE sp_500 = TRUE").fetchall()
    # Iterate through the result set
    for row in result:
        stock = yf.Ticker(row[0])
        try:
            get_equities_market_data(stock)
        except:
            pass
