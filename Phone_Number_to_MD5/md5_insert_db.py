# coding:utf-8

import argparse
import io
import mysql.connector

parser = argparse.ArgumentParser(description='''将MD5码写入数据库''')
parser.add_argument('-f', '--file', metavar='file', help='指定MD5文件')
args = parser.parse_args()
# args.file = '133.csv'

config = {
    'host': '10.10.208.192',  # 连接的IP地址
    'user': 'cuile',
    'password': 'Cuile@2018',
    'port': 3306,
    'database': 'feinno',
    'charset': 'utf8',  # 编码格式,防止查出来的数据中文乱码
}
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    with io.open(args.file, mode='r') as f:
        for line in f:
            d = line.strip().split(',')
            # print(d[0], d[1])
            try:
                cursor.execute("insert delayed into md5 (phone_number, md5) values ('%s','%s')" % (d[0], d[1]))
                conn.commit()
            except Exception as e:
                print(d[0], d[1], ";", e)
            # break
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()
