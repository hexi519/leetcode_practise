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
    def isBalanced(self, root):
        balanced, _ = self.helper(root, 1)
        return balanced

    def helper(self, root, height):
        if not root:
            return True, height

        else:
            banlanceL, heightL = self.helper(root.left, height + 1)
            banlanceR, heightR = self.helper(root.right, height + 1)

            return True if banlanceL and banlanceR and heightL >= heightR - 1 and heightL <= heightR + 1 else False, max(heightL, heightR)


if __name__ == "__main__":
    sol = Solution()
    print(f"res is {sol.isBalanced(tt)}")  # true
    print(f"res is {sol.isBalanced(less_skew)}")  # true
    print(f"res is {sol.isBalanced(dt)}")  # true
    print(f"res is {sol.isBalanced(skew)}")  # false
    print(f"res is {sol.isBalanced(None)}")  # true
    print(f"res is {sol.isBalanced(TreeNode(3))}")  # True
