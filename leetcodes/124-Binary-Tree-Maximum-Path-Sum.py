# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard] binary-tree
'''

from typing import Dict, List
from util import *
# from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from sys import maxsize as MAX_INT

MIN_INT = -(MAX_INT - 1)


class Solution:
    val = MIN_INT

    def maxPathSum(self, root: TreeNode) -> int:
        max(self.helper(root))
        return self.val

    def helper(self, root):
        # corner
        if not root:
            return MIN_INT, MIN_INT

        l_w, l_o = self.helper(root.left)
        r_w, r_o = self.helper(root.right)

        cur_w_all = root.val + (l_w if l_w > 0 else 0) + (r_w if r_w > 0 else 0)
        cur_w = root.val + max(l_w if l_w > 0 else 0, r_w if r_w > 0 else 0)
        cur_o = max(l_o, l_w, r_o, r_w)
        self.val = max(self.val, cur_w_all, cur_o)
        # print(f"root({root.val}) with (cur_w,cur_o) of ({cur_w},{cur_o})")
        return cur_w, cur_o


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPathSum(less_skew))
    print(sol.maxPathSum(TreeNode(-3)))