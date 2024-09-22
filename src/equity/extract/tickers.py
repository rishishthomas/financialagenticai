import financedatabase as fd
import duckdb
import pandas as pd

# Initialize the Equities database
equities = fd.Equities()

companies_df = equities.select()
companies_df = companies_df.reset_index()
print(companies_df.head())

sp500_companies_df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
print(sp500_companies_df.head())
companies_df['sp_500'] = companies_df['symbol'].isin(sp500_companies_df['Symbol'])
companies_df = companies_df.drop_duplicates(subset='symbol', keep='first')


print(companies_df.head())

with duckdb.connect("../../../db/equities.db") as con:
    con.sql("CREATE TABLE companies AS SELECT * FROM companies_df")
    con.sql("INSERT INTO companies SELECT * FROM companies_df")
    #con.table("ticker_profile").show()



