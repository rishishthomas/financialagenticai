from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import duckdb
import llm.llm_query as llm_query


app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route('/process', methods=['GET'])
@cross_origin(supports_credentials=True)
def process():
    try:
        # Get the 'query' parameters from the request
        question = request.args.get('query')
        print("question: " + question)
        sql = llm_query.get_results_open_ai(question)
        print("sql: " + sql)

        with duckdb.connect("../db/equities.db") as con:
            # Run a query to get data from the table
            df = con.execute(sql).df()
            # Iterate through the result set
        json_return =  jsonify(df.to_dict(orient='records'))
        print("json: " + str(json_return))
        return json_return
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide numerical values."}), 400

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

