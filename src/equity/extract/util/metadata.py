from ftplib import print_line

import duckdb


def create_table_insert_data(table_name):
    with duckdb.connect("../../../db/equity.db") as con:
        try:
            con.sql("CREATE TABLE table_description AS SELECT '" + table_name + "' as table_name, * FROM (DESCRIBE " + table_name + ")")
        except:
            pass
        try:
            con.sql("INSERT INTO table_description SELECT '" + table_name + "' as table_name, * FROM (DESCRIBE " + table_name + ")")
        except:
            pass

def build_db_metadata():
    with duckdb.connect("../../../db/equity.db") as con:
        for table_name in [ "analyst_price_targets",
                            "balance_sheet",
                            "calendar",
                            "cashflow",
                            "companies",
                            "earnings_dates",
                            "earnings_estimate",
                            "earnings_history",
                            "eps_revisions",
                            "eps_trend",
                            "growth_estimates",
                            "historical_meta_data",
                            "income_stmt",
                            "insider_purchases",
                            "insider_roster_holders",
                            "insider_transactions",
                            "institutional_holders",
                            "major_holders",
                            "mutualfund_holders",
                            "quarterly_balance_sheet",
                            "quarterly_income_stmt",
                            "recommendations",
                            "revenue_estimate",
                            "sec_filings",
                            "upgrades_downgrades"
                           ]:
            create_table_insert_data(table_name)

def print_metadata():
    with duckdb.connect("../../../db/equity.db") as con:
        # Run a query to get data from the table
        result = con.execute("select * from table_description").fetchall()
        table_details = {}
        for row in result:
            if row[0] not in table_details:
                table_details[row[0]] = [row]
            else:
                table_details[row[0]].append(row)

        for key, value in table_details.items():
            print("TABLE " + key + "(")
            for row in value:
                print("   " + row[1] + " " + row[2] + "," + " -- " + key + " " + str(row[1]))
            print_line(")")
            print_line(" ")



print_metadata()