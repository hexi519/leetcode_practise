# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative , 只有iterative比较有难度
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        >>> sol = Solution()
        >>> sol.postorderTraversal(None)
        []
        >>> sol.postorderTraversal(tt)
        [4, 5, 3]
        >>> sol.postorderTraversal(skew)
        [2, 1, 5, 3]
        """
        from queue import deque
        nodeStack = deque([root])
        ans = []

        while len(nodeStack):
            cur = nodeStack.pop()
            ans.extend( [cur.val] if cur else [] )
            nodeStack.extend( [cur.left,cur.right] if cur else [] )

        return ans[::-1]            
        

        