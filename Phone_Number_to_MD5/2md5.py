# coding:utf-8

import argparse
import csv
import hashlib
import io
import os
import textwrap

import common

parser = argparse.ArgumentParser(description=textwrap.dedent(
    '''
    生成手机号对应的MD5
    
    将3位手机号段内的所有号码转为MD5码，生成“3位号段+.csv”的文件
    shell: ./2md5 -r 133
    result: 133.csv 

    或 

    将文本文件内包含的手机号（每行一个）转为MD5码，生成“文本文件名+.md5”的文件
    shell: ./2md5 -f xxx
    result: xxx.md5
    '''
), formatter_class=argparse.RawTextHelpFormatter)
group = parser.add_mutually_exclusive_group()
group.add_argument('-r', metavar="range", dest="range", type=int, help='手机号号段')
group.add_argument("-f", metavar="file", dest="file", type=str, help="包含手机号的文件")
args = parser.parse_args()

common.timing_starts()
if args.range:
    s = int(args.range) * 100000000
    e = (int(args.range) + 1) * 100000000
    with io.open(str(args.range) + '.csv', 'wt') as f:
        csv_writer = csv.writer(f)
        for i in range(s, e):
            pn = str(i)
            csv_writer.writerow([pn, hashlib.md5(pn.encode(encoding='utf-8')).hexdigest()])

elif args.file:
    (filename, extension) = os.path.splitext(args.file)
    with io.open(args.file, 'rt')as rf, io.open(filename + ".md5", 'wt')as wf:
        csv_reader = csv.reader(rf)
        csv_writer = csv.writer(wf)
        for r in csv_reader:
            csv_writer.writerow(hashlib.md5(r[0].encode(encoding='utf-8')).hexdigest().upper())

else:
    print("usage: -h or --help arguments show help message")
common.timing_ends()
