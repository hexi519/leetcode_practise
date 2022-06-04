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


def buildTree(arrs):
    if len(arrs) == 0:
        return None

    maxVal, maxIdx = 0, 0
    for i in range(len(arrs)):
        if maxVal < arrs[i]:
            maxVal, maxIdx = arrs[i], i

    root = TreeNode(maxVal)
    root.left = buildTree(arrs[:maxIdx])
    root.right = buildTree(arrs[maxIdx + 1:])

    return root


class Solution:

    def constructMaximumBinaryTree(self, nums):
        return buildTree(nums)


if __name__ == "__main__":
    sol = Solution()
    tree = sol.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    preTraverse(tree)

    tree = sol.constructMaximumBinaryTree([3, 2, 1])
    preTraverse(tree)
