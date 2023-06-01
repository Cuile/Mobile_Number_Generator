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
    # 读取路径下的所有CSV文件名
    csv_files = [name for name in os.listdir(path)
                if name.endswith('.csv')]
    # 随机行号生成范围
    a = 1
    b = 100000000
    # 每次随机读取的号码个数
    random_step = 1000
    rows = [0]
    # 生成输出文件
    with open(path + '/' + 'random.out', 'a') as t:
        # csv_writer = csv.writer(t)
        # while len(rows) != 0:
        rows = []
        print('待处理行号 {}~{}'.format(a, b))
        
        for f in csv_files:
            
            # 随机选择一个文件，从中随机读取random_step个号码
            file = path + '/' + random.choice(csv_files)
            print('处理文件：{}'.format(file))
            
            # 生成随机读取的行数列表
            line_no = []
            for i in range(random_step):
                line_no.append(random.randint(a, b))
            # 对行数列表去重
            line_no = set(line_no)
            # print(line_no)
            
            # 读取文件，找到line_no包含的行号
            i = 0
            with open(file) as f_read:
                for line in f_read:
                    i += 1
                    if i in line_no:
                        rows.append(line)
                print('读取行完成')
        
        # 随机排序rows
        random.shuffle(rows)
        # print(rows)

        # for i in rows:
            # csv_writer.writerow([i])
        t.writelines(rows)
        print('写入随机排序号码 {} 个'.format(len(rows)))
        # 随机行号范围，减去刚处理过的行数
        b -= random_step
        print(15 * '=')