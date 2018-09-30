# coding:utf-8

import logging
import hashlib
import argparse
import textwrap

parser = argparse.ArgumentParser(description=textwrap.dedent('''生成手机号对应的MD5'''),
                                 epilog="前台使用：./2md5 -r 133 \n"
                                        "后台使用：nohup ./2md5 -r 133 > 133.log 2>&1 & \n",
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-r', metavar='range', help='手机号号段')
args = parser.parse_args()

LOG_FORMAT = "%(message)s"
logging.basicConfig(filename=args.range + '.csv', level=logging.INFO, format=LOG_FORMAT)

s = int(args.range) * 100000000
e = (int(args.range) + 1) * 100000000
for i in range(s, e):
    phone_number = str(i)
    logging.info(phone_number + "," + hashlib.md5(phone_number.encode(encoding='utf-8')).hexdigest())
