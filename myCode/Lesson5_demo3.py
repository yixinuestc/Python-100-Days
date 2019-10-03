"""
Lesson5  完美数

Author: yixin

"""
# -*- coding=utf-8 -*-
range_lower = 2
range_upper = int(input('输入上线'))

print("完美数有：",end="")
for i in range(range_lower, range_upper + 1):
    sum = 1
    num_sqrt = int(i ** 0.5)
    for j in range(2,num_sqrt + 1):
        if i % j == 0:
            sum += j + (i // j)

    if sum == i:
        print("%d " %(i), end="")