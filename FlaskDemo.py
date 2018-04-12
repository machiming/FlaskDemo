from flask import Flask, json

import query

app = Flask(__name__)


@app.route('/<start>/<end>')
def hello_world(start, end):
    sql = "select * from mobile limit " + start + "," + end
    result = query.querysVal(sql)
    return json.dumps(result, ensure_ascii=False)

@app.route('/phone/<phoneN>')
def checkPhone(phoneN):
    sql = "select * from mobile where phone="+phoneN[0:7]
    print(phoneN[0:7])
    result = query.querysVal(sql)
    return json.dumps(result, ensure_ascii=False)

@app.route('/login')
def login():
    return '{hello:hello}'


if __name__ == '__main__':
    app.run(port=8999, host='0.0.0.0', debug='true')
