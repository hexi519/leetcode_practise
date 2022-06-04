# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy] bt
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def maxDepth(self, root):
        if not root: return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    sol = Solution()
    print(f"res is {sol.maxDepth(less_skew)}")  # 3
    print(f"res is {sol.maxDepth(BST)}")  # 4
    print(f"res is {sol.maxDepth(skew)}")  # 3
    print(f"res is {sol.maxDepth(None)}")  # 0
    print(f"res is {sol.maxDepth(TreeNode(4))}")  # 1
