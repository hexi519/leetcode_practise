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
    def sumOfLeftLeaves(self, root) -> int:
        leaf, sum = self.helper(root)
        return sum if not leaf else 0

    def helper(self, root):
        if not root:
            return False, 0

        if not root.left and not root.right:
            # print(f"\tleaf returns {root.val}")
            return True, root.val

        else:
            leafL, sumL = self.helper(root.left)
            leafR, sumR = self.helper(root.right)
            # print(f"curNode of {root.val} is {sumL + (0 if leafR else sumR)}")
            return False, sumL + (0 if leafR else sumR)


if __name__ == '__main__':
    sol = Solution()
    print(f"res is {sol.sumOfLeftLeaves(BST)}")
    print(f"res is {sol.sumOfLeftLeaves(skew)}")
    print(f"res is {sol.sumOfLeftLeaves(TreeNode(3))}")
