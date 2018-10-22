# coding:utf-8

import argparse
import csv
import hashlib
import io
import logging
import os
import textwrap

parser = argparse.ArgumentParser(description=textwrap.dedent('''
                                                            生成手机号对应的MD5\n
                                                            ./2md5 -r 133\n
                                                            ./2md5 -f xxx
                                                            '''), formatter_class=argparse.RawTextHelpFormatter)
group = parser.add_mutually_exclusive_group()
group.add_argument('-r', metavar="range", dest="range", type=int, help='手机号号段')
group.add_argument("-f", metavar="file", dest="file", type=str, help="包含手机号的文件")
args = parser.parse_args()

LOG_FORMAT = "%(message)s"
if args.range:
    logging.basicConfig(filename=str(args.range) + '.csv', level=logging.INFO, format=LOG_FORMAT)

    s = int(args.range) * 100000000
    e = (int(args.range) + 1) * 100000000
    for i in range(s, e):
        phone_number = str(i)
        logging.info(phone_number + "," + hashlib.md5(phone_number.encode(encoding='utf-8')).hexdigest())

elif args.file:
    (filename, extension) = os.path.splitext(args.file)
    logging.basicConfig(filename=filename + '.md5', level=logging.INFO, format=LOG_FORMAT)
    with io.open(args.file, 'rt')as rf:
        csv_reader = csv.reader(rf)
        for r in csv_reader:
            logging.info(hashlib.md5(r[0].encode(encoding='utf-8')).hexdigest())

else:
    print("usage: -h or --help arguments show help message")
