# -*- coding: utf-8 -*-
import hashlib
import csv
import os
import random

# 生成hash值
def getHash(hash: str, value: str):
    if hash == 'md5':
        return hashlib.md5(value.encode(encoding='utf-8')).hexdigest()
    elif hash == 'sha256':
        return hashlib.sha256(value.encode(encoding='utf-8')).hexdigest()

# 根据号段生成号码及hash值
def make_ragne(r: int, path: str, hash=None):
    s = r * 100000000
    e = (r + 1) * 100000000
    target_file = path + "/" + str(r) + '.csv'
    print('生成文件' + target_file)
    with open(target_file, 'wt') as f:
        csv_writer = csv.writer(f)
        if hash:
            for i in range(s, e):
                pn = str(i)
                csv_writer.writerow([pn, getHash(hash, pn)])
        else:
            for i in range(s, e):
                pn = str(i)
                csv_writer.writerow([pn])

# 生成随机行号集合
def get_random_lineno(a: int, b: int, step: int):
    # 生成随机读取的行数列表
    line_no = []
    try:
        for i in range(step):
            line_no.append(random.randint(a, b))
        # 对行数列表去重
        # print(line_no)
        return set(line_no)
    except ValueError as err:
        print('无法生成随机行号集合，请重新设置随机行号范围')
        return set(line_no)

# 读取文件，找到line_no包含的行号
# 使用临时文件，保存未选中的行
def get_random_line(file: str, line_no: set, path: str):
    rows = []
    i = 0
    with open(file, 'r') as f_read:
        # 删除现存的tmp文件
        with os.popen('rm -f {}'.format(path + '/tmp')) as p:
            p.read()
        with open(path + '/tmp', 'a') as tmp_csv:
            for line in f_read:
                i += 1
                if i in line_no:
                    rows.append(line)
                else:
                    tmp_csv.write(line)
    print('读取行完成')
    
    # 使用tmp_csv替换file
    with os.popen('rm -f {} && mv {} {}'.format(file, path + '/tmp', file), 'r') as p:
        p.read()
    return rows

# 读取路径下的所有CSV文件名
def get_random_files(path: str):
    # csv_files = [name for name in os.listdir(path)
    #             if name.endswith('.csv')]
    with os.popen('wc -l ' + path + '/*.csv') as p:
        files = p.read()
    files = files.splitlines()
    files.pop()
    # print(files)
    csv_lineno = []
    csv_files = []
    for i in files:
        t = i.strip().split(' ')
        csv_lineno.append(t[0])
        csv_files.append(t[1])
    return csv_files, int(max(csv_lineno))

# 随机排序已生成的手机号码
def make_random(path: str):
    # 生成输出文件
    with open(path + '/random.out', 'a') as out:
        rows = [0]
        step = 1000000
        while len(rows) != 0:
            rows = []

            csv_files, max_lineno = get_random_files(path)
            # print(get_random_files(path))
            
            # 每次随机读取的号码个数
            if (step > 10) and (step > max_lineno):
                step //= 10
            print('待处理行号 {}~{}，每个文件读取 {} 行'.format(1, max_lineno, step))

            for f in csv_files:
                # 随机选择一个文件，从中随机读取random_step个号码
                # file = path + '/' + random.choice(csv_files)
                # 选择一个文件，从中随机读取random_step个号码
                print('处理文件：{}'.format(f), end='')

                line_no = get_random_lineno(1, max_lineno, step)
                rows = get_random_line(f, line_no, path)
            
            # 随机排序rows
            random.shuffle(rows)
            # print(rows)
            # 写入输出文件
            out.writelines(rows)
            out.flush()
            print('写入随机排序号码 {} 个'.format(len(rows)))
            
            print(15 * '=')
            
            # 测试时使用，保证while只循环一次
            # rows = []
        else:
            print('号码合并随机排序完成')