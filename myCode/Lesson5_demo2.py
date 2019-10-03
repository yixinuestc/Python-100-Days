"""
Lesson5  百钱白鸡

Author: yixin
鸡翁 5钱一只    最多20
鸡母 3钱一只    最多33
雏鸡 1钱三只   肯定为三的倍数 最多99
"""
# -*- coding=utf-8 -*-
for a in range(3,100,3):  # 雏鸡数量
    for b in range(1,min(21,100 - a)):  # 公鸡数量
        c = 100 - a - b  # 母鸡数量
        if c == 0:
            continue
        if 5 * b + 3 * c + a // 3 == 100:
            print("公鸡数量:%d,母鸡数量:%d,雏鸡数量:%d" %(b,c,a))





