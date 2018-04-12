from flask import Flask, json

import query

app = Flask(__name__)


@app.route('/<start>/<end>')
def hello_world(start, end):
    sql = 'select * from mobile limit ' + start+","+end
    print(sql)
    result = query.querys(sql)
    return json.dumps(result, ensure_ascii=False)


@app.route('/login')
def login():
    return '{hello:hello}'


if __name__ == '__main__':
    app.run(port=8999, host='0.0.0.0', debug='true')
