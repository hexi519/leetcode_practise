# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] bt
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

        while len(nodes):
            tmpNodes = []

            idx = 0
            while idx < len(nodes):
                curNode = nodes[idx]
                if curNode.left:
                    tmpNodes.append(curNode.left)

                if curNode.right:
                    tmpNodes.append(curNode.right)

                curNode.next = None if idx == len(nodes) - 1 else nodes[idx + 1]
                idx += 1

            nodes = tmpNodes

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