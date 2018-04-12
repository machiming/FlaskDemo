import pymysql
import config

def querys(sql):
    conn = pymysql.connect(
        host=config.database['host'],
        port=config.database['port'],
        user=config.database['user'],
        passwd=config.database['passwd'],
        db=config.database['db'],
        charset=config.database['charset']
    )
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

def querysVal(sql):
    conn = pymysql.connect(
        host=config.database['host'],
        port=config.database['port'],
        user=config.database['user'],
        passwd=config.database['passwd'],
        db=config.database['db'],
        charset=config.database['charset']
    )
    cursor = conn.cursor()
    cursor.execute(sql)
    row_1 = cursor.fetchall()
    cursor.close()
    return row_1