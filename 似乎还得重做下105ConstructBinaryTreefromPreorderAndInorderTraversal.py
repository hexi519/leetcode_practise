<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   []
'''

from typing import Dict, List
from util import *

# 题目都没有讲清楚，要求是重建二叉树，并返回其根节点

"""
    shortest codes without cutting pre-order --> taking advantage of python's character
    https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/401124/Python-easy-solution-with-comments
"""

class Solution:
    """
    >>> preorder = [3,9,20,15,7]
    >>> inorder = [9,3,15,20,7]
    >>> s = Solution()
    >>> rootNode = s.buildTree(preorder,inorder)
    >>> rootNode.val
    3
    >>> s.traverse(rootNode)    
    3 9 20 15 7 
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        assert (len(preorder) == len(inorder))
        if (len(preorder) == 0):
            return None
        rootNode = TreeNode(preorder[0])
        # find index in inorder
        rootIndex = inorder.index(preorder[0])
        # split into two parts
        lenLeft = rootIndex - 0
        lenRight = len(inorder) - rootIndex
        rootNode.left = self.buildTree(preorder[1:1 + lenLeft], inorder[0:rootIndex])  
        rootNode.right = self.buildTree(preorder[1 + lenLeft:], inorder[rootIndex + 1:])

        return rootNode

    def traverse(self, root:TreeNode) :
        if(root==None):
            return 
        print(root.val,end =" ")
        self.traverse(root.left)
        self.traverse(root.right)


=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   []
'''

from typing import Dict, List
from util import *

# 题目都没有讲清楚，要求是重建二叉树，并返回其根节点

"""
    shortest codes without cutting pre-order --> taking advantage of python's character
    https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/401124/Python-easy-solution-with-comments
"""

class Solution:
    """
    >>> preorder = [3,9,20,15,7]
    >>> inorder = [9,3,15,20,7]
    >>> s = Solution()
    >>> rootNode = s.buildTree(preorder,inorder)
    >>> rootNode.val
    3
    >>> s.traverse(rootNode)    
    3 9 20 15 7 
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        assert (len(preorder) == len(inorder))
        if (len(preorder) == 0):
            return None
        rootNode = TreeNode(preorder[0])
        # find index in inorder
        rootIndex = inorder.index(preorder[0])
        # split into two parts
        lenLeft = rootIndex - 0
        lenRight = len(inorder) - rootIndex
        rootNode.left = self.buildTree(preorder[1:1 + lenLeft], inorder[0:rootIndex])  
        rootNode.right = self.buildTree(preorder[1 + lenLeft:], inorder[rootIndex + 1:])

        return rootNode

    def traverse(self, root:TreeNode) :
        if(root==None):
            return 
        print(root.val,end =" ")
        self.traverse(root.left)
        self.traverse(root.right)


>>>>>>> hesy/master
