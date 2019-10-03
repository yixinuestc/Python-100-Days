"""
Lesson5 craps赌博游戏
玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；
如果点数和为2、3或12，则玩家输庄家胜。
若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄家胜

Author: yixin
"""

# -*- coding=utf-8 -*-
import random

gameOver = False
while(gameOver is False):
    a = random.randint(1, 6)
    b = random.randint(1,6)
    print("The dice number are %d %d" %(a,b))
    if a + b == 7 or a + b == 11:
        print("You win")
        gameOver = True
    elif a + b == 2 or a + b == 3 or a + b == 12:
        print("You loss")
        gameOver = True
