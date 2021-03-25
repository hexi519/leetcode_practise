# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root : return root

        def help_sort(root,par,dir):
            if dir == "left":   # return 最右边的子节点，且向右边的分支传递孩子
                if root.left:   # 左边的话 左子树没有就无所谓
                    root.left=help_sort(root.left,root,"left")
                if root.right:
                    returnNode = help_sort(root.right,root,"right")
                    return returnNode
                else:
                    root.right=par
                    return root

            elif dir == "right":    # return 最右边的子节点，且向右边的分支传递孩子
                
                
                if root.left:   # 左边的话 左子树没有就无所谓
                    root.left=help_sort(root.left,root,"left")
                else:
                    root.left=par
                    

                if root.right:
                    root.right = help_sort(root.right,root,"right")
                    return returnNode
                else:
                    root.rc=par
                    return root
            else:
                raise ValueError(f"dir只能是left或者right，这里是{dir}")
                



        if root.left:
            root.left = help_sort(root.left,root)

        if root.right:
            help_sort(root.left,root)



        

        