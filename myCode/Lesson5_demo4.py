"""
Lesson5  斐波那契数列

Author: yixin

"""
# -*- coding=utf-8 -*-
n = int(input('输入个数'))
a,b = 1,1

for i in range(1,n + 1):
    print("%d " % a, end="")
    c = a + b
    a,b = b,c


