# -*- coding: utf-8 -*-
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
        print("生成随机数完成...", end="", flush=True)
        return set(line_no)
    except ValueError:
        print("无法生成随机数集合，请重新设置随机数范围")
        return set(line_no)


def get_csv_info(path: str) -> tuple:
    """读取路径下的所有CSV文件行数

    Args:
        path (str): 路径地址

    Returns:
        tuple: csv文件名列表和所有文件中最大行数的值
    """
    csv_lineno = []
    csv_files = []
    # 使用 wc 命令读取文件行数
    with os.popen("wc -l " + path + "/*.csv") as p:
        files = p.read()
    files = files.splitlines()
    for i in files:
        t = i.strip().split(" ")
        # 删除汇总行
        if t[1] != "total":
            csv_lineno.append(t[0])
            csv_files.append(t[1])
    return csv_files, int(max(csv_lineno))


def read_random_rows(file: str, line_no: set, path: str) -> list:
    """读取文件中指定行的内容

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
        lines = []
        i = 0
        for row in f_read:
            i += 1
            if i in line_no:
                lines.append(row)
            else:
                tmp_csv.write(row)
        print("读取 {:,} 行完成".format(len(lines)))
    # 使用tmp_csv替换file
    with os.popen(
        "rm -f {} && mv {} {}".format(file, path + "/tmp", file),
    ) as p:
        p.read()
    return lines
