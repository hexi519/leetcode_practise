# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root):
        if not root: return root
        nodes = [root]
        num = 1

        while num:
            tmpNum = 0
            tmpNodes = []

            idx = 0
            # print(f"nodes is {[node.val if node else 'None' for node in nodes]}")
            while idx < len(nodes):
                curNode = nodes[idx]
                if curNode:
                    tmpNum += 1
                    if curNode.left:
                        tmpNodes.append(curNode.left)
                    if curNode.right:
                        tmpNodes.append(curNode.right)

                    if idx == len(nodes) - 1:
                        curNode.next = None

                    else:
                        curNode.next = nodes[idx + 1]
                    """
                    curNode.next = None
                    nextIdx = idx + 1
                    # if idx % 2 == 0:  # even +1
                    #     nextIdx = idx + 1
                    # else:
                    #     nextIdx = idx + 2

                    while nextIdx < len(nodes) and not nodes[nextIdx]:
                        nextIdx += 1

                    if nextIdx < len(nodes):
                        curNode.next = nodes[nextIdx]

                        # print(f"\tnode {curNode.val}'s nextIdx is {nextIdx} of {nodes[nextIdx]}")

                else:
                    tmpNodes.extend([None, None])

                    """
                idx += 1

            nodes = tmpNodes
            num = tmpNum

        return root

    def traverse(self, root):
        if not root:
            return root

        line = [root]
        while len(line):
            tmp = []
            for node in line:
                print(f"{node.val}.next is {node.next.val if node.next else 'None'}")
                if node.left:
                    tmp.append(node.left)

                if node.right:
                    tmp.append(node.right)

            line = tmp


if __name__ == "__main__":
    sol = Solution()
    sol.connect(BST)
    sol.traverse(BST)
    # sol.connect(dt)
    # sol.traverse(dt)
