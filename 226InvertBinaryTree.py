# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy]翻转二叉树
'''

from typing import Dict, List
from util import *

################################
########### 自己的代码 ##########
################################
# 居然已经和大佬的一致了....
class Solution:
    """
    >>> sol = Solution()
    >>> sol.traverse_tree(s)
    '#4 #2 #1 None None #3 None None #7 None None'
    >>> sol.invertTree(s)
    >>> sol.traverse_tree(s)
    '#4 #7 None None #2 #3 None None #1 None None'
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        
        return root 

    def traverse_tree(self, s):
        """for test"""
        if s:
            return f"#{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"
        return None

################################
########### 栈的代码 ##########
################################
# 用栈 巧思 但是速度反而还没有之前的快,,,
class Solution:
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root