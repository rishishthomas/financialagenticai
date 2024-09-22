from flask import jsonify
import duckdb
import equities.llm.llm_query as llm_query

question = "give me all sp 500 stocks with p/e below 10"
sql = llm_query.get_results_open_ai(question)
print("sql: " + sql)

with duckdb.connect("../db/equity.db") as con:
    # Run a query to get data from the table
    df = con.execute(sql).df()
    # Iterate through the result set
json_return =  jsonify(df.to_dict(orient='records'))
print("json: " + str(json_return))
