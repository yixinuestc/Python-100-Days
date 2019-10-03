"""
辗转相除法求最大公约数和最小公倍数

Author: yixin
"""
# -*- coding=utf-8 -*-


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b,a % b)


if __name__ == '__main__':
    a = int(input("输入一个正整数"))
    b = int(input("输入另一个正整数"))
    c = gcd(max(a,b),min(a,b))  # 求最大公约数
    d = a * b // c
    print("%d 和 %d的最大公约数为%d,最小公倍数为%d" %(a,b,c,d))