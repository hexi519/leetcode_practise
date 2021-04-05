# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy] 235Lowest-Common-Ancestor-of-a-Binary-Search-Tree.py
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution:
    def lowestCommonAncestor(self, root, one, sec):
        """
        >>> s = Solution()
        >>> BST == s.lowestCommonAncestor(BST,BST_left,BST_right)
        True
        >>> BST_left == s.lowestCommonAncestor(BST,BST__left,BST_left)
        True
        """
        # recursive
        p, q = (one.val, sec.val) if one.val < sec.val else (sec.val, one.val)
        if p < root.val < q or root.val == p or root.val == q:
            return root

        if q < root.val:
            return self.lowestCommonAncestor(root.left, one, sec)

        if p > root.val:
            return self.lowestCommonAncestor(root.right, one, sec)