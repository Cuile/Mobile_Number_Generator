# -*- coding: utf-8 -*-
import time
import hashlib
import csv
import os
import random


# 计时函数
start = startTime = end = endTime = bar = None
def timing_starts():
    global start, startTime
    start = time.clock()
    startTime = time.time()
def timing_ends():
    global end, endTime
    end = time.clock()
    endTime = time.time()
    print("-------------------------------------------------------------------------")
    print("CPU Running time: {fs:.2f}s".format(fs=(end - start)))
    print("Script Running time: {fs:.2f}s".format(fs=(endTime - startTime)))
    print("-------------------------------------------------------------------------")

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

# 随机排序已生成的手机号码
def make_random(path: str):
    csv_files = [name for name in os.listdir(path)
                if name.endswith('.csv')]
    r = []
    a = 1
    b = 100000000
    # 每次随机读取的号码个数
    random_step = 10
    with open(path + '/' + 'random.out', 'a') as t:
        """ csv_writer = csv.writer(t)
        for i in range(10):
            row = os.popen('sed -n {}p {}'.format(random.randint(a, b), path + '/' + random.choice(csv_files))).read(11)
            if row == '':
                b -= 1
            else:
                r.append(row)
            # csv_writer.writerow([row])
        print(r) """

        rows = []
        for i in range(1):
            # 随机选择一个文件，从中随机读取random_step个号码
            # 生成随机读取的行数列表
            line_no = []
            for i in range(random_step):
                line_no.append(random.randint(a, b))
            # 对行数列表去重、排序
            line_no = sorted(set(line_no))
            # print(line_no)
            
            cli_sea = ''
            cli_del = ''
            file = path + '/' + random.choice(csv_files)
            for i in line_no:
                cli_sea += '-e {}p '.format(i)
                cli_del += '-e {}d '.format(i)
            cli_sea = 'sed -n {} {}'.format(cli_sea, file)
            cli_del = 'sed -i {} {}'.format(cli_del, file)
            print(cli_sea)
            print(cli_del)
            # 读取sed命令返回的行
            row = os.popen(cli_sea).read()
            # print(row)
            row = row.split('\n')
            # print(row)
            rows += row
            # 删除sed命令已读取的行
            print(os.popen(cli_del).read())
        
        # 删除空元素
        rows = list(filter(None, rows))
        # 随机排序rows
        random.shuffle(rows)
        print(rows)
        print(len(rows))
