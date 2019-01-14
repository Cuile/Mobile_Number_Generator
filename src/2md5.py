# coding:utf-8

import argparse
import csv
import hashlib
import io
import os
import textwrap

import common


def getHash(hash: str, value: str):
    if hash == 'md5':
        return hashlib.md5(value.encode(encoding='utf-8')).hexdigest()
    elif hash == 'sha256':
        return hashlib.sha256(value.encode(encoding='utf-8')).hexdigest()


parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(title='子命令')

make_parse = subparsers.add_parser('make',
                                   help='生成校验码',
                                   description=textwrap.dedent('''
                                                                生成手机号对应的哈希值
                                                                '''),
                                   epilog=textwrap.dedent('''
                                    =======================================================================
                                    使用方法：
                                    
                                    1.将3位手机号段内的所有号码生成MD5码，生成“3位号段+.csv”的文件
                                    use: ./2md5 -r 133 --hash md5 -tf 133
                                    out: 133.csv
                                
                                    2.将文本文件内包含的手机号（每行一个）生成sha256码，生成“文本文件名+.sha256”的文件
                                    use: ./2md5 -sf source_file --hash sha256 -tf target_file
                                    out: target_file.sha256
                                    =======================================================================
                                                            '''),
                                   formatter_class=argparse.RawTextHelpFormatter)
group = make_parse.add_mutually_exclusive_group()
group.add_argument('-r',
                   metavar="range",
                   dest="range",
                   type=int,
                   help='手机号号段')
group.add_argument('-sf', '--source_file',
                   metavar="source_file",
                   dest="source_file",
                   type=str,
                   help='手机号源文件')
make_parse.add_argument("--hash",
                        metavar="hash",
                        action='store',
                        choices={'md5', 'sha256'},
                        help="校验算法")
make_parse.add_argument('-tf', '--target_file',
                        metavar="target_file",
                        dest="target_file",
                        type=str,
                        help="生成的目标文件")

check_parse = subparsers.add_parser('check',
                                    help='校验设备码')
group = check_parse.add_mutually_exclusive_group()
group.add_argument('-s',
                   metavar="code",
                   dest="code",
                   type=str,
                   help='设备码')
group.add_argument('-sf', '--source_file',
                   metavar="source_file",
                   dest="source_file",
                   type=str,
                   action='store',
                   help='设备码源文件')
check_parse.add_argument('-t', '--type',
                         metavar='type',
                         dest="type",
                         type=str,
                         action='store',
                         choices={'imei', 'emid'},
                         help="设备码类型")
check_parse.add_argument('-tf', '--target_file',
                         metavar="target_file",
                         dest="target_file",
                         action='store',
                         type=str,
                         help="生成的目标文件")

args = parser.parse_args()

common.timing_starts()
if args.range:
    s = int(args.range) * 100000000
    e = (int(args.range) + 1) * 100000000
    with io.open(str(args.range) + '.csv', 'wt') as f:
        csv_writer = csv.writer(f)
        for i in range(s, e):
            pn = str(i)
            csv_writer.writerow([pn, getHash(args.h, pn)])
elif args.file:
    (filename, extension) = os.path.splitext(args.file)
    with io.open(args.file, 'rt')as rf, io.open(filename + "." + args.h, 'wt')as wf:
        csv_reader = csv.reader(rf)
        csv_writer = csv.writer(wf)
        for r in csv_reader:
            csv_writer.writerow([getHash(args.h, r[0])])
elif not args.h:
    print()
    print("usage: -h or --help arguments show help message")
    print()
else:
    print()
    print("usage: -h or --help arguments show help message")
    print()
common.timing_ends()
