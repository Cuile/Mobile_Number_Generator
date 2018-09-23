import logging
import hashlib
import argparse

parser = argparse.ArgumentParser(description='''生成手机号对应的MD5''')
parser.add_argument('-f', '--logFileName', metavar='logFileName', help='生成的日志文件')
parser.add_argument('-r', '--range', metavar='range', help='手机号号段')
args = parser.parse_args()

LOG_FORMAT = "%(message)s"
logging.basicConfig(filename=args.logFileName, level=logging.INFO, format=LOG_FORMAT)
# logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

r = int(args.range)
start = r * 100000000
end = (r + 1) * 100000000 - 1

for i in range(start, end):
    phone_number = str(i)
    logging.info(phone_number + "," + hashlib.md5(phone_number.encode(encoding='utf-8')).hexdigest())
