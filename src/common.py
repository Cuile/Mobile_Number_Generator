# -*- coding: utf-8 -*-
import csv
import hashlib
import os
import random


def get_Hash(hash: str, value: str) -> str:
    """生成校验值

    Args:
        hash (str): 校验方法
        value (str): 被校验字符串

    Returns:
        str: 校验字符串。如校验方法错，则返回错误提示。
    """
    if hash == "md5":
        return hashlib.md5(value.encode(encoding="utf-8")).hexdigest()
    elif hash == "sha256":
        return hashlib.sha256(value.encode(encoding="utf-8")).hexdigest()
    else:
        return "hash set error!"


def get_random_number_set(min: int, max: int, count: int) -> set:
    """生成随机数集合

    Args:
        min (int): 随机数最小值
        max (int): 随机数最大值
        count (int): 总生成数量

    Returns:
        set: 生成的随机数集合
    """
    line_no = []
    try:
        for i in range(count):
            line_no.append(random.randint(min, max))
        return set(line_no)
    except ValueError:
        print("无法生成随机数集合，请重新设置随机数范围")
        return set(line_no)


def read_rows(file: str, line_no: set, path: str) -> list:
    """读取文件中，指定行的内容

    Args:
        file (str): 要读取文件名
        line_no (set): 指定行号的集合
        path (str): 文件所在的路径

    Returns:
        list: 指定行的内容
    """
    with open(file, "r", newline="") as f_read, open(
        path + "/tmp", "w", newline=""
    ) as tmp_csv:
        reader = csv.reader(f_read)
        writer = csv.writer(tmp_csv)
        lines = []
        tmp_lines = []
        i = 0
        for row in reader:
            i += 1
            if i in line_no:
                lines.append(row)
            else:
                tmp_lines.append(row)
        print("读取 {} 行完成".format(i))
        writer.writerows(tmp_lines)
    # 使用tmp_csv替换file
    with os.popen(
        "rm -f {} && mv {} {}".format(file, path + "/tmp", file),
    ) as p:
        p.read()
    return lines


def get_csv_info(path: str) -> tuple:
    """读取路径下的所有CSV文件名

    Args:
        path (str): 路径地址

    Returns:
        tuple: csv文件名列表和所有文件中最大行数的值
    """
    # csv_files = [name for name in os.listdir(path)
    #             if name.endswith('.csv')]
    with os.popen("wc -l " + path + "/*.csv") as p:
        files = p.read()
    files = files.splitlines()
    files.pop()
    # print(files)
    csv_lineno = []
    csv_files = []
    for i in files:
        t = i.strip().split(" ")
        csv_lineno.append(t[0])
        csv_files.append(t[1])
    return csv_files, int(max(csv_lineno))


def make_range(r: int, path: str, hash: str = "") -> None:
    """根据号段生成号码及hash值

    Args:
        r (int): 号段前3位，比如 139
        path (str): 生成文件的保存路径
        hash (str, optional): 校验方法，如指定，则同时生成校验码。 Defaults to "".
    """
    print("准备 {} 号段数据...".format(r))
    s = r * 100000000
    e = (r + 1) * 100000000
    target_file = path + "/" + str(r) + ".csv"
    with open(target_file, "w", newline="") as f:
        pn = []
        if hash == "":
            for i in range(s, e):
                pn.append("".join([str(i), "\n"]))
        else:
            for i in range(s, e):
                pn.append(",".join([str(i), "".join([get_Hash(hash, str(i)), "\n"])]))
        print("开始写入文件...")
        f.writelines(pn)
        f.close()
    print("写入文件完成 {}".format(target_file))


def make_random(path: str) -> None:
    """随机排序已生成的手机号码
    随机排序完成，结果输出到random.out。

    Args:
        path (str): 已生成数码的路径
    """
    # 生成输出文件
    with open(path + "/random.out", "a", newline="") as out:
        writer = csv.writer(out)
        count = 1000000
        rows = [0]
        while len(rows) != 0:
            rows = []

            csv_files, max_lineno = get_csv_info(path)
            # print(get_file_info(path))

            # 每次随机读取的号码个数
            if (count > 10) and (count > max_lineno):
                count //= 10
            print("待处理行数 {}，每个文件计划读取 {} 行".format(max_lineno, count))

            for f in csv_files:
                # 随机读取文件，从中随机读取random_step个号码
                # f = path + '/' + random.choice(csv_files)

                # 顺序读取文件，从中随机读取random_step个号码
                print("处理文件：{} ...... ".format(f), end="")

                line_no = get_random_number_set(1, max_lineno, count)
                rows += read_rows(f, line_no, path)

            # 随机排序rows
            random.shuffle(rows)
            # 写入输出文件
            # out.writelines(rows)
            # out.flush()
            writer.writerows(rows)

            print("写入随机排序号码 {} 个".format(len(rows)))
            print(30 * "=")

            # 测试时使用，保证while只循环一次
            # rows = []
        else:
            print("号码合并随机排序完成")
