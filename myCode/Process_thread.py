"""
顺序执行
"""
"""
# -*- coding=utf-8 -*-
from time import time

def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()
"""

"""
多进程处理
"""

"""
from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    main()
"""

"""
多线程
"""
# -*- coding=utf-8 -*-
from time import time
from threading import Thread
import numpy as np

class CounterThread(Thread):
    def __init__(self,blks):
        super().__init__()
        self._blks = blks
        self._counter = 0

    def run(self):
        for i in range(0,len(self._blks)):
            self._counter += self._blks[i]

    @property
    def counter(self):
        return self._counter

def main():
    nThread = 8  # thread number
    num_blks = 100000000 // nThread
    number_list = np.zeros((nThread,num_blks),dtype=np.int64)

    threads = []
    for i in range(0,nThread):
        for j in range(0,num_blks ):
            number_list[i][j] = i * num_blks + j + 1
        tt = CounterThread(number_list[i])
        threads.append(tt)
        tt.start()

    start = time()
    for t in threads:
        t.join()

    total = 0
    for t in threads:
        total += t.counter
    
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == '__main__':
    main()




