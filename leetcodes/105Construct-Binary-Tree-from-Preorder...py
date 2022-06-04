# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''
from util import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:

        allLen = len(preorder)
        if not allLen: return None
        if allLen == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        # find index
        index = 0
        for idx, node in enumerate(inorder):
            if node == root.val:
                index = idx
                break

        root.left = self.buildTree(preorder[1:1 + index], inorder[:index])
        root.right = self.buildTree(preorder[1 + index:], inorder[index + 1:])

        return root
