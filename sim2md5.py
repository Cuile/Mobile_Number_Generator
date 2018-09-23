import logging
import hashlib
import argparse

parser = argparse.ArgumentParser(description='''生成手机号对应的MD5''')
# parser.add_argument('-f', '--logFileName', metavar='logFileName', help='生成的日志文件')
parser.add_argument('-r', '--range', metavar='range', help='手机号号段')
args = parser.parse_args()

LOG_FORMAT = "%(message)s"
logging.basicConfig(filename=args.range + '.csv', level=logging.INFO, format=LOG_FORMAT)

for i in range(int(args.range) * 100000000, (int(args.range) + 1) * 100000000):
    phone_number = str(i)
    logging.info(phone_number + "," + hashlib.md5(phone_number.encode(encoding='utf-8')).hexdigest())
