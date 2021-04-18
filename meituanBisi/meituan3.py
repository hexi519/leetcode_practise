# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [3]
'''

from typing import Dict, List
from util import *
# from loguru import logger as log

# 第一行输入操作个数，下面输入n个数组
from collections import defaultdict
operationNum = int(input())
# logic
curNum = 0
idx2kind = [None]*1000  # idx2kind[0]="A"
kind2idx = dict()  # kind2idx["A"]=0
kind2con = defaultdict(list)  # kind2con["A"].append(1)

for oper in range(operationNum):
    # data process
    info = input().split()

    if info[0] == "1":  # 插入
        trainidx, kind = int(info[1]), info[2]

        if not kind in kind2con.keys():  # 未出现过
            idx2kind[curNum] = kind
            kind2idx[kind] = curNum
            curNum += 1

        kind2con[kind].append(trainidx)

    elif info[0] == "2":  # 交换
        kind1, kind2 = info[1], info[2]
        idx1, idx2 = kind2idx[kind1], kind2idx[kind2]
        kind2idx[kind1], kind2idx[kind2] = idx2, idx1
        idx2kind[idx1], idx2kind[idx2] = kind2, kind1

# print(f"******* curNum is {curNum}")
# print(f"******* idx2kind is {idx2kind[:5]}")
# print(f"******* kind2idx is {kind2idx}")
# print(f"******* kind2con is {kind2con}")
for i in range(curNum):
    kindd = idx2kind[i]
    for itIdx, it in enumerate(kind2con[kindd]):
        if i == 0 and itIdx==0:  # 第一个
            print(it,end="")
        else:
            print(" "+str(it),end="")

"""
7
1 1 A
1 2 B
1 5 A
1 3 C
1 4 D
2 A B
2 B C

"""