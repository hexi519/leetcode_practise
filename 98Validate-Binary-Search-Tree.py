# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution:
    # info : bool , (min,max)
    def isValidBST(self, root: TreeNode) -> bool:
        """
        >>> s = Solution()
        >>> s.isValidBST(tt)
        False
        >>> s.isValidBST(BST)
        True
        >>> s.isValidBST(None)
        False
        """
        if not root:
            return False

        def help_recur(root):
            lc, lmin, lmax = True, 1232323, 1232323
            rc, rmin, rmax = True, 1232323, 1232323
            if root.left:
                lc, lmin, lmax = help_recur(root.left)
            # print(f"help_recur(root.left) returns {help_recur(root.left)}")
            if lc and root.right:
                rc, rmin, rmax = help_recur(root.right)

            if not root.left:
                if not root.right:
                    return True, root.val, root.val
                return rc and rmin > root.val, root.val, rmax

            if not root.right:
                return lc and root.val > lmax, lmin, root.val
            
            return lc and rc and lmax<root.val<rmin, lmin ,rmax

        return help_recur(root)[0]
