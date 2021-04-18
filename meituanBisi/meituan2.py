# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [2]
'''

from typing import Dict, List
from util import *
# from loguru import logger as log


# 第一行输入操作个数，下面输入n个数组
anum, bnum, k = [int(i) for i in input().split()]

asum, bsum = 0, 0
for _ in range(anum):
    number, fight = [int(i) for i in input().split()]
    if fight >= k:
        asum += number*fight

for _ in range(bnum):
    number, fight = [int(i) for i in input().split()]
    if fight >= k:
        bsum += number*fight

print("A" if asum>bsum else "B" )

"""
3 4 3
3 1
3 4
6 2
2 4
3 1
1 5
4 2
"""
"""
1 1 1
1 300
2 100
"""