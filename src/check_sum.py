# coding:utf-8

import re


def make_it_complete(imei_str: str):
    # 奇数位之和
    even_Sum = 0
    # 偶数位之和
    odd_Sum = 0
    for i in range(len(imei_str)):
        if (i + 1) % 2 == 0:
            odd_Sum += ((int(imei_str[i]) * 2) // 10) + ((int(imei_str[i]) * 2) % 10)
        else:
            even_Sum += int(imei_str[i])
    check_code = (10 - ((odd_Sum + even_Sum) % 10))
    check_code = 0 if check_code == 10 else check_code
    return ''.join([imei_str, str(check_code)])


def getCheckCode(type: str, imei: str):
    if type == 'imei':
        # 判断 imei 为14位数字
        if re.match(r'^\d{14}$', imei):
            # 返回 True,完整的imei
            return {'check': True, 'imei': make_it_complete(str(imei))}
        # 判断 imei 为15位数字
        elif re.match(r'^\d{15}$', imei):
            # 取前14位数字，进行校验
            complete_imei = make_it_complete(re.match(r'^(\d{14})\d$', imei).group(1))
            # 判断校验后的值是否相等
            if imei == complete_imei:
                # 返回 True,原始的imei
                return {'check': True, 'imei': imei}
            else:
                # 返回 False,正确的imei
                return {'check': False, 'imei': complete_imei}
        else:
            # 返回 False,imei为None
            return {'check': False, 'imei': None}
    elif type == 'emid':
        pass
    else:
        raise RuntimeError('getCheckCode type error')
