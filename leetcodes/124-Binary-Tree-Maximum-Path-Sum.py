# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard] binary-tree
'''

from typing import Dict, List
from util import *
from loguru import logger as log

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


def helper(root):
    # corner
    if not root:
        return MIN_INT, MIN_INT

    l_w, l_o = helper(root.left)
    r_w, r_o = helper(root.right)
    cur_w = root.val + (l_w if l_w > 0 else 0) + (r_w if r_w > 0 else 0)
    cur_o = max(l_o, l_w, r_o, r_w)
    # print(f"root({root.val}) with (cur_w,cur_o) of ({cur_w},{cur_o})")
    return cur_w, cur_o


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return max(helper(root))
        """
        m_l, m_r = self.maxPathSum(root.left), self.maxPathSum(root.right)
        if root.val >= 0:
            # m_cur = root.val+(m_l if m_l>0 else 0) +(m_r if m_r>0 else 0)
            m_cur = root.val + m_l + m_r
            self.val = max(self.val, m_cur)
            return m_cur
        else:
            m_cur = max(m_l + m_r + root.val, m_l, m_r, 0)
            self.val = max(self.val, m_cur)
            return m_cur
        """


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPathSum(TreeNode(-3)))
    # print(sol.maxPathSum(tt))