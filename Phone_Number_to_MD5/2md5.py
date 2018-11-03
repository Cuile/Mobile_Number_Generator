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
    生成手机号对应的哈希值
    '''
), epilog=textwrap.dedent(
    '''
    =======================================================================
    使用方法：
    
    1.将3位手机号段内的所有号码生成MD5码，生成“3位号段+.csv”的文件
    in : ./2md5 -r 133 md5
    out: 133.csv 

    2.将文本文件内包含的手机号（每行一个）生成sha256码，生成“文本文件名+.sha256”的文件
    in : ./2md5 -f xxx sha256
    out: xxx.md5
    =======================================================================
    '''
), formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("h", metavar="hash", type=str, help="摘要算法，md5、sha1、sha224、sha256、sha384、sha512")
group = parser.add_mutually_exclusive_group()
group.add_argument('-r', metavar="range", dest="range", type=int, help='手机号号段')
group.add_argument("-f", metavar="file", dest="file", type=str, help="包含手机号的文件")
args = parser.parse_args()
hashlib.algorithms_available


def getHash(hash: str, value: str):
    return eval("hashlib.{hash}('{value}'.encode(encoding='utf-8')).hexdigest().upper()".format(hash=hash, value=value))


if args.range:
    common.timing_starts()

    s = int(args.range) * 100000000
    e = (int(args.range) + 1) * 100000000
    with io.open(str(args.range) + '.csv', 'wt') as f:
        csv_writer = csv.writer(f)
        for i in range(s, e):
            pn = str(i)
            csv_writer.writerow([pn, getHash(args.h, pn)])

    common.timing_ends()
elif args.file:
    common.timing_starts()

    (filename, extension) = os.path.splitext(args.file)
    with io.open(args.file, 'rt')as rf, io.open(filename + "." + args.h, 'wt')as wf:
        csv_reader = csv.reader(rf)
        csv_writer = csv.writer(wf)
        for r in csv_reader:
            csv_writer.writerow([getHash(args.h, r[0])])

    common.timing_ends()
elif not args.h:
    print()
    print("usage: -h or --help arguments show help message")
    print()
else:
    print()
    print("usage: -h or --help arguments show help message")
    print()
