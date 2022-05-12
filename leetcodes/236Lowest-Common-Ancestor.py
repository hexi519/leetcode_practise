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
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root   # 如果没找到就是None，找到就是返回找到的点
        
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
        if not left:    return right    
        if not right:   return left
        
        """ original codes suck
        ans = None

        def helpFind(root, p, q):   # true or false --> tuple(False,False)
            nonlocal ans
            findp, findq = False, False
            if not root or ans:
                print(f"\t已经存在ans，返回" if root else "\t到叶节点的子节点，返回")
                return findp, findq

            print(f"root is {root.val}")

            findp_, findq_ = helpFind(root.left, p, q)
            print(f"\t{root.val}:搜索左子节点:{findp_}, {findq_}")
            findp, findq = findp or findp_, findq or findq_

            if (findp or findq) and (root == p or root == q):
                ans = root
                print(f"\t{root.val}:findp,finq is {findp},{findq} and root is as well.")
                return True, True

            findp_, findq_ = helpFind(root.right, p, q)   # 这样写能砍掉不少
            print(f"\t{root.val}:搜索右子节点:{findp_}, {findq_}")
            findp, findq = findp or findp_, findq or findq_
            if findp and findq:  # 只有两边都遍历过了的情况才有会这个
                print(f"\t{root.val}:左右找到了")
                ans = root if not ans else ans
                return findp, findq

            if (findp or findq) and (root == p or root == q):
                ans = root if not ans else ans
                print(f"\t{root.val}:findp,finq is {findp},{findq} and root is as well.")
                return True, True

            return findp or root==p, findq or root==q

        helpFind(root,p,q)

        return ans
        """