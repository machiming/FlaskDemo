from flask import Flask, json, request

import query

app = Flask(__name__)


@app.route('/')
def a():
    return '请传值'

#post get请求
@app.route('/gp', methods=["get","post"])
def hello_world():
   if request.method=="get":
       print(request.args['user'])
   elif request.method=="post":
       print(request.form['user'])

    #sql查询
   sql = "select * from mobile limit 0,5"
   result = query.querysVal(sql)
   return json.dumps(result, ensure_ascii=False)

#传参函数
@app.route('/phone/<phoneN>')
def checkPhone(phoneN):
    sql = "select * from mobile where phone=" + phoneN[0:7]
    result = query.querysVal(sql)
    return json.dumps(result, ensure_ascii=False)


@app.route('/login')
def login():
    return '{hello:hello}'


if __name__ == '__main__':
    app.run(port=8999, host='0.0.0.0', debug='true')
