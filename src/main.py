# coding:utf-8

import argparse
import textwrap

import common

# import pysnooper


# @pysnooper.snoop()
def main():
    try:
        if args.function == "make_range":
            if not args.path:
                args.path = "."
            if args.range:
                common.make_range(args.range, args.path)
            else:
                raise RuntimeError("-r 未设置")
        elif args.function == "make_random":
            if not args.path:
                raise RuntimeError("-p 参数未指定")
            else:
                common.make_random(args.path)
                # cProfile.run('common.make_random(args.path)', sort = 'cumtime')
        # 以下代码未做调试
        """ 
        elif args.function == "make_hash":
            if not args.path:
                args.path = "."
            if args.number:
                if args.hash:
                    print(
                        {
                            "number": args.number,
                            args.hash: hash.getHash(args.hash, str(args.number)),
                        }
                    )
                else:
                    raise RuntimeError("--hash 未设置")
            # 按号段生成号码
            elif args.range:
                s = int(args.range) * 100000000
                e = (int(args.range) + 1) * 100000000
                target_file = args.path + "/" + str(args.range) + ".csv"
                print(target_file)
                with open(target_file, "wt") as f:
                    csv_writer = csv.writer(f)
                    if args.hash:
                        for i in range(s, e):
                            pn = str(i)
                            csv_writer.writerow([pn, hash.getHash(args.hash, pn)])
                    else:
                        for i in range(s, e):
                            pn = str(i)
                            csv_writer.writerow([pn])
            elif args.source_file:
                (filename, extension) = os.path.splitext(args.source_file)
                with open(args.source_file, "rt") as rf, open(
                    filename + "." + args.hash, "wt"
                ) as wf:
                    csv_reader = csv.reader(rf)
                    csv_writer = csv.writer(wf)
                    for r in csv_reader:
                        csv_writer.writerow([hash.getHash(args.hash, r[0])])
            else:
                raise RuntimeError("请使用 -n 或 -r 或 -sf 设置参数")
        elif args.function == "check":
            if args.type:
                if args.code:
                    print(
                        {
                            "code": args.code,
                            args.type: check_sum.getCheckCode(
                                args.type, str(args.code)
                            )[args.type],
                        }
                    )
                elif args.source_file:
                    (filename, extension) = os.path.splitext(args.source_file)
                    with open(args.source_file, "rt") as rf:
                        csv_reader = csv.reader(rf)
                        if args.target_file:
                            # 将设备码类型，做为输出文件后缀
                            with open(
                                "{filename}.{ext}".format(
                                    filename=filename, ext=args.type
                                ),
                                "wt",
                            ) as wf:
                                csv_writer = csv.writer(wf)
                                for r in csv_reader:
                                    csv_writer.writerow(
                                        [
                                            check_sum.getCheckCode(
                                                args.type, str(r[0])
                                            )[args.type]
                                        ]
                                    )
                        else:
                            for r in csv_reader:
                                print(
                                    {
                                        "code": args.code,
                                        args.type: check_sum.getCheckCode(
                                            args.type, str(r[0])
                                        )[args.type],
                                    }
                                )
                else:
                    raise RuntimeError("请使用 -c 或 -sf 设置参数")
            else:
                raise RuntimeError("-t 或 --type 未设置")
        else:
            raise RuntimeError("请使用 make 或 check 命令") 
        """
    except RuntimeError as err:
        print(
            textwrap.dedent(
                """
                {err}
                usage: -h or --help arguments show help message
                """.format(err=err)
            )
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=textwrap.dedent("""生成手机号和对应的校验码""")
    )
    subparsers = parser.add_subparsers(title="子命令", dest="function")

    make_range = subparsers.add_parser(
        "make_range",
        help="根据手机号段生成手机号码",
        description=textwrap.dedent("""根据手机号段生成手机号码"""),
        epilog=textwrap.dedent(
            """
            use: ./mng make_range -r 139 -p ./data
            out: ./data/139.csv
            """
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    make_range.add_argument(
        "-r",
        "--range",
        metavar="range",
        dest="range",
        type=int,
        action="store",
        help="手机号段前3位，如133",
    )
    make_range.add_argument(
        "-p",
        "--path",
        metavar="path",
        dest="path",
        type=str,
        action="store",
        help="生成文件的保存路径",
    )

    make_random = subparsers.add_parser(
        "make_random",
        help="随机排序已生成的手机号码",
        description=textwrap.dedent("""随机排序已生成的手机号码"""),
        epilog=textwrap.dedent(
            """
            use: ./mng make_random -p ./data
            out: ./data/randomout.csv
            """
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    make_random.add_argument(
        "-p",
        "--path",
        metavar="path",
        dest="path",
        type=str,
        action="store",
        help="需要排序的文件路径",
    )

    # make_hash = subparsers.add_parser('make_hash', help='生成号码hash值', description=textwrap.dedent('''生成手机号对应的hash值'''),
    #                                    epilog=textwrap.dedent('''
    #                                     =======================================================================
    #                                     使用方法：

    #                                     1.将3位手机号段内的所有号码生成MD5码，生成“3位号段+.csv”的文件
    #                                     use: ./2md5 -n 13901234567 --hash md5
    #                                     out: 133.csv

    #                                     2.将文本文件内包含的手机号（每行一个）生成sha256码，生成“文本文件名+.sha256”的文件
    #                                     use: ./2md5 -sf source_file --hash sha256 -tf target_file
    #                                     out: target_file.sha256
    #                                     =======================================================================
    #                                                             '''), formatter_class=argparse.RawTextHelpFormatter)
    # make_hash.add_argument("--hash", metavar="hash", dest='hash', type=str, action='store', choices={'md5', 'sha256'}, help="校验算法")
    # make_hash.add_argument('-p', '--path', metavar="path", dest="path", action='store', help="生成文件的保存路径")
    # make_hash_group = make_hash.add_mutually_exclusive_group()
    # make_hash_group.add_argument('-n', '--number', metavar="number", dest="number", type=int, action='store', help='手机号码')
    # make_hash_group.add_argument('-r', '--range', metavar="range", dest="range", type=int, action='store', help='手机号号段前3位，如 133')
    # make_hash_group.add_argument('-sf', '--source_file', metavar="source_file", dest="source_file", type=str, action='store', help='手机号源文件')

    # check_parse = subparsers.add_parser('check',
    #                                     help='校验设备码',
    #                                     description=textwrap.dedent('''校验手机的设备码'''),
    #                                     epilog=textwrap.dedent(''''''),
    #                                     formatter_class=argparse.RawTextHelpFormatter)
    # check_parse.add_argument('-t', '--type', metavar='{imei|emid}', dest="type", type=str, action='store',
    #                          choices={'imei', 'emid'}, help="设备码类型")
    # check_parse.add_argument('-tf', '--target_file', dest="target_file", action='store_true', help="生成的目标文件")
    # check_group = check_parse.add_mutually_exclusive_group()
    # check_group.add_argument('-c', '--code', metavar="code", dest="code", type=str, action='store', help='设备码')
    # check_group.add_argument('-sf', '--source_file', metavar="source_file", dest="source_file", type=str, action='store',
    #                          help='设备码源文件')

    args = parser.parse_args()
    main()
