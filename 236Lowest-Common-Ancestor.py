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
        """
        """
        ans = None

        def helpFind(root, p, q):   # true or false --> tuple(False,False)
            nonlocal ans
            findp, findq = False, False
            if not root or ans:
                print(f"\t已经存在ans，返回" if root else "到根节点，返回")
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
                ans = root
                return findp, findq

            if (findp or findq) and (root == p or root == q):
                ans = root
                print(f"\t{root.val}:findp,finq is {findp},{findq} and root is as well.")
                return True, True

            return findp, findq

        helpFind(root,p,q)

        return ans
