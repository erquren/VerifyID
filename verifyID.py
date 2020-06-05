#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 16:46
# @Author  : Erquren
# @File    : verifyID.py
class IdentityCard:
    def __init__(self):
        self.__Wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        self.__Ti = ['1', '0', 'x', '9', '8', '7', '6', '5', '4', '3', '2']

    def check(self, code):
        if len(code) != 17:
            print("必须为17位的字符")
            return False
        return True

    def calculate(self, code):
        sum = 0
        for i in range(17):
            sum += int(code[i]) * self.__Wi[i]
        return self.__Ti[sum % 11]


def test():
    ic = IdentityCard()
    code = "10000000000000000"  # 17位身份证
    if ic.check(code):
        print("你的校验位为:%s" % ic.calculate(code))


def get_woman_id():
    ic = IdentityCard()
    year = list(range(1980, 2000))
    month = []
    for i in range(1, 13):
        month.append("%02d" % i)
    pre = []
    for i in range(len(year)):
        for j in range(len(month)):
            pre.append(str(year[i]) + str(month[j]))
    for i in range(len(pre)):
        code = "440532" + pre[i] + '23281'
        if ic.check(code):
            if ic.calculate(code) == '9':
                print(code + '9')


if __name__ == '__main__':
    # test()
    get_woman_id()
