# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]236Lowest-Common-Ancestor-of-a-Binary-Tree.py
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution:
    # 原始版
    def ori_slowestCommonAncestor(self, root, p, q):
        if not root:  #or root == p or root == q:
            return root  # 如果没找到就是None，找到就是返回找到的点

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:  # 左右都有返回，说明自己就是最近公共祖先
            return root

        if root.val == p.val or root.val == q.val:  # 这个可以移到最前面去，能省一些时间
            return root

        if not left:
            return right

        if not right:
            return left

    # 根据原始版优化的版本
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root  # 如果没找到就是None，找到就是返回找到的点

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:  # 左右都有返回，说明自己就是最近公共祖先
            return root
        """
        这两种情况都各自蕴含着两种情况：
        1. 非空的那支本身就是指向非空的指向祖先，也就是要返回的答案
        2. 非空的那支只含有一个节点
        1的话直接返回没问题。
        2的话，后续会被 if left and right的判断更新返回的root值
        """
        if not left: return right
        if not right: return left
