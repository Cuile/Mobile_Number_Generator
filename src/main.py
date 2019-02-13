# coding:utf-8

import argparse
import csv
import os
import textwrap

import check_sum
import common
import hash

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='子命令', dest='function')

make_parse = subparsers.add_parser('make', help='生成校验码', description=textwrap.dedent('''生成手机号对应的校验码'''),
                                   epilog=textwrap.dedent('''
                                    =======================================================================
                                    使用方法：
                                    
                                    1.将3位手机号段内的所有号码生成MD5码，生成“3位号段+.csv”的文件
                                    use: ./2md5 -n 13901234567 --hash md5
                                    out: 133.csv
                                    
                                    2.将文本文件内包含的手机号（每行一个）生成sha256码，生成“文本文件名+.sha256”的文件
                                    use: ./2md5 -sf source_file --hash sha256 -tf target_file
                                    out: target_file.sha256
                                    =======================================================================
                                                            '''), formatter_class=argparse.RawTextHelpFormatter)
make_parse.add_argument("--hash", metavar="hash", dest='hash', type=str, action='store', choices={'md5', 'sha256'},
                        help="校验算法")
make_parse.add_argument('-tf', '--target_file', dest="target_file", action='store_true', help="生成的目标文件")
make_group = make_parse.add_mutually_exclusive_group()
make_group.add_argument('-n', '--number', metavar="number", dest="number", type=int, action='store', help='手机号码')
make_group.add_argument('-r', '--range', metavar="range", dest="range", type=int, action='store', help='手机号号段前3位，如 133')
make_group.add_argument('-sf', '--source_file', metavar="source_file", dest="source_file", type=str, action='store',
                        help='手机号源文件')

check_parse = subparsers.add_parser('check',
                                    help='校验设备码',
                                    description=textwrap.dedent('''校验手机的设备码'''),
                                    epilog=textwrap.dedent(''''''),
                                    formatter_class=argparse.RawTextHelpFormatter)
check_parse.add_argument('-t', '--type', metavar='{imei|emid}', dest="type", type=str, action='store',
                         choices={'imei', 'emid'}, help="设备码类型")
check_parse.add_argument('-tf', '--target_file', dest="target_file", action='store_true', help="生成的目标文件")
check_group = check_parse.add_mutually_exclusive_group()
check_group.add_argument('-c', '--code', metavar="code", dest="code", type=str, action='store', help='设备码')
check_group.add_argument('-sf', '--source_file', metavar="source_file", dest="source_file", type=str, action='store',
                         help='设备码源文件')

args = parser.parse_args()

# print(args)

common.timing_starts()
try:
    if args.function == 'make':
        if args.hash:
            if args.number:
                print({'number': args.number, args.hash: hash.getHash(args.hash, str(args.number))})
            elif args.range:
                s = int(args.range) * 100000000
                e = (int(args.range) + 1) * 100000000
                with open(str(args.number) + '.csv', 'wt') as f:
                    csv_writer = csv.writer(f)
                    for i in range(s, e):
                        pn = str(i)
                        csv_writer.writerow([pn, hash.getHash(args.h, pn)])
            elif args.source_file:
                (filename, extension) = os.path.splitext(args.source_file)
                with open(args.source_file, 'rt')as rf, open(filename + "." + args.h, 'wt')as wf:
                    csv_reader = csv.reader(rf)
                    csv_writer = csv.writer(wf)
                    for r in csv_reader:
                        csv_writer.writerow([hash.getHash(args.h, r[0])])
            else:
                raise RuntimeError('请使用 -t 或 -r 或 -sf 设置参数')
        else:
            raise RuntimeError('--hash 未设置')
    elif args.function == 'check':
        if args.type:
            if args.code:
                print({'code': args.code, args.type: check_sum.getCheckCode(args.type, str(args.code))[args.type]})
            elif args.source_file:
                (filename, extension) = os.path.splitext(args.source_file)
                with open(args.source_file, 'rt') as rf:
                    csv_reader = csv.reader(rf)
                    if args.target_file:
                        with open('{filename}.{ext}'.format(filename=filename, ext=args.type), 'wt') as wf:
                            csv_writer = csv.writer(wf)
                            for r in csv_reader:
                                csv_writer.writerow([check_sum.getCheckCode(args.type, str(r[0]))[args.type]])
                    else:
                        for r in csv_reader:
                            print(
                                {'code': args.code, args.type: check_sum.getCheckCode(args.type, str(r[0]))[args.type]})
            else:
                raise RuntimeError('请使用 -c 或 -sf 设置参数')
        else:
            raise RuntimeError('-t 或 --type 未设置')
    else:
        raise RuntimeError('请使用 make 或 check 命令')
except RuntimeError as err:
    print(textwrap.dedent('''
        {err}
        usage: -h or --help arguments show help message
        '''.format(err=err)))

common.timing_ends()
