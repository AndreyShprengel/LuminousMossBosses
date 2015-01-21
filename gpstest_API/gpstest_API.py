from flask import Flask, url_for
from sqlalchemy import create_engine, select
from json import dumps

app = Flask(__name__)

HOST = 'localhost'
USER = 'web_test'
PASSWORD = 'sileneidene'
DATABASE = 'gpstest'

def query_database(query):
    gps_eng = create_engine('mysql://%s:%s@%s/%s' % (USER, PASSWORD, HOST, DATABASE), echo=True)
    gps_conn = gps_eng.connect()
    query_result = gps_conn.execute(query)
    return query_result 

def result_to_json(query_result):
    column_names = query_result.keys()
    row_list = []
    for row in query_result:
        i = 0
        row_dict = {}
        for item in row:
            #the split is used to do away with the 'u' that 
            #sqlalchemy puts in front of every key name
            row_dict[str(column_names[i]).split('\'')[0]] = str(item)
            i += 1
        row_list.append(row_dict)
    #replace single quote with double for valid json
    json_result = str(row_list).replace('\'', '"')
    return json_result

@app.route('/')
def api_root():
    return 'Welcome\n'

@app.route('/test_records')
def api_test_records():
    result = query_database('SELECT * FROM test_data WHERE model_number = \'test\'')
    #be aware that this call will close the result object, and it will not be useable afterward.
    items = result_to_json(result)
    return items 

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid + '\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
