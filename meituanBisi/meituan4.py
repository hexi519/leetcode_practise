# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [4]
'''

from typing import Dict, List
from util import *
# from loguru import logger as log

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"{self.val},({self.left}),({self.right})"

    def __doc__(self):
        return f"{self.val},({self.left}),({self.right})"

ans = 0
def traverse(root):
    # print(f"cur node is {root.val},({root.left}),({root.right})")
    leftNum,rightNum,unvisited_l,unvisited_r=0,0,0,0
    leftNum4left,rightNum4left,unvisted_l4left,unvisted_r4left =0,0,0,0
    leftNum4ight,rightNum4ight,unvisted_l4right,unvisted_r4right  =0,0,0,0
    if root.left:
        # print(f"\t enter left")
        leftNum4left,rightNum4left,unvisted_l4left,unvisted_r4left = traverse(nodes[root.left])
        leftNum =  leftNum4left+rightNum4left+1# 每次只算子节点,没包括其本身
        # leftNum = traverse(root.left)[0]+1 # 每次只算子节点,没包括其本身
    if root.right: 
        # print(f"\t enter right")
        leftNum4right,rightNum4right,unvisted_l4right,unvisted_r4right = traverse(nodes[root.left])
        rightNum =  leftNum4right+rightNum4right+1# 每次只算子节点,没包括其本身
        
    if root.val <=0:
        unvisited_l += leftNum
    else:
        if root.right:
            unvisited_r+=unvisted_r4right + leftNum4right if root.val>=nodes[root.right].val else unvisted_l4right

        if root.left:
            unvisited_l+=unvisted_l4left + rightNum4left if root.val <=nodes[root.left].val else unvisted_r4left
    
    return leftNum,rightNum, unvisited_l,unvisited_r


# 第一行输入操作个数，下面输入n个数组
nodeNum, relaNum, rootIdx = [int(i) for i in input().split()]
relas = []
for relation in range(relaNum):
    relas.append([int(i) for i in input().split()])

vals = [0]
vals.extend([int(i) for i in input().split()])
print(f"values is {vals}")
curIdx = 0

nodes = [None]*(nodeNum+1)
for i in range(len(nodes)):
    nodes[i] = TreeNode(0)

for rela in relas:  # [1,2,3]   index of node   # 建立树
    nodes[rela[0]].val = vals[rela[0]]
    nodes[rela[1]].val = vals[rela[1]]
    nodes[rela[2]].val = vals[rela[2]]
    nodes[rela[0]].left = rela[1]   # 用index记录了
    nodes[rela[0]].right = rela[2]

_,_,left,right = traverse(nodes[rootIdx])
print(left+right)
"""
7 3 1
1 2 3
2 4 5
3 6 7
10 5 5 10 5 5 10
"""