"""
Lesson5 水仙花数

Author: yixin
"""
# -*- coding=utf-8 -*-
print("三位数的水仙花数有：",end="")
for i in range(101,1000):
    a = i // 100  # 百位
    b = (i - a * 100) // 10  # 十位
    c = i % 10   # 个位
    if (a ** 3) + (b ** 3) + (c ** 3) == i:
        print('%d '%(i),end="")



