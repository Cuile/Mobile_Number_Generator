# -*- coding: utf-8 -*-
import csv
import random

import lib


def make_range(range_list: list, path: str, hash: str = "") -> None:
    """根据号段生成号码及hash值

    Args:
        range_list (list): 号段前3位，如 [139,138]
        path (str): 生成文件的保存路径
        hash (str, optional): 校验方法，如指定，则同时生成校验码。 Defaults to "".
    """
    for r in range_list:
        print("准备 {} 号段数据...".format(r))
        s = r * 100000000
        e = (r + 1) * 100000000
        pn = []
        if hash == "":
            for i in range(s, e):
                pn.append("".join([str(i), "\n"]))
        else:
            for i in range(s, e):
                pn.append(
                    ",".join([str(i), "".join([lib.get_Hash(hash, str(i)), "\n"])])
                )
        print("开始写入文件...")
        target_file = path + "/" + str(r) + ".csv"
        with open(target_file, "w", newline="") as f:
            f.writelines(pn)
        print("写入文件完成 {}".format(target_file))


def make_random(path: str) -> None:
    """随机排序已生成的手机号码
    随机排序完成，结果输出到random.out。

    Args:
        path (str): 已生成数码的路径
    """
    # count = 1000000
    count = 10000
    rows = [0]
    while len(rows) != 0:
        rows = []

        csv_files, max_lineno = lib.get_csv_info(path)
        # print(get_file_info(path))

        # 每次随机读取的号码个数
        if (count > 10) and (count > max_lineno):
            count //= 10
        print(
            "待处理数据总数 {:,} 行，每个文件计划读取 {:,} 行。".format(
                max_lineno, count
            )
        )

        for f in csv_files:
            # 随机读取文件，从中随机读取random_step个号码
            # f = path + '/' + random.choice(csv_files)

            # 顺序读取文件，从中随机读取random_step个号码
            print("处理文件：{}......".format(f), end="", flush=True)

            line_no = lib.get_random_number_set(1, max_lineno, count)
            rows += lib.read_rows(f, line_no, path)

        # 随机排序rows
        random.shuffle(rows)
        # 生成输出文件
        with open(path + "/random.out", "a", newline="") as out:
            writer = csv.writer(out)
            # 写入输出文件
            # out.writelines(rows)
            # out.flush()
            writer.writerows(rows)

        print("写入随机排序号码 {:,} 个".format(len(rows)))
        print(30 * "=")

        # 测试时使用，保证while只循环一次
        rows = []
    else:
        print("号码合并随机排序完成")
