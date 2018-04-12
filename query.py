import pymysql
from config import database as db


def querys(sql):
    conn = pymysql.connect(db['host'], db['user'], db['passwd'], db['db'], db['port'], charset=db['charset'])
    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    return row


def querysVal(sql):
    conn = pymysql.connect(db['host'], db['user'], db['passwd'], db['db'], db['port'], charset=db['charset'])
    cursor = conn.cursor()
    cursor.execute(sql)
    index = cursor.description
    result = []
    for res in cursor.fetchall():
        row = {}
        for i in range(len(index) - 1):
            row[index[i][0]] = res[i]
        result.append(row)
    conn.close()
    return result
