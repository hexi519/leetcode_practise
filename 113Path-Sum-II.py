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
    # recursive
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        >>> sol = Solution()
        >>> sol.pathSum(s,8)
        [[3, 4, 1], [3, 5]]
        >>> sol.pathSum(None,8)
        []
        >>> sol.pathSum(skew,3)
        []
        """
        #! 这里注意回溯和dfs区别
        """
        这里一直用的是一个res和一个path和一个tmpSum
        回溯属于dfs的一种实现。回溯比普通dfs好的一个地方在于，回溯会有一个维护数据结构的情况，很多dfs是采用
            dfs(root.left, sum-root.val, ls+[root.val], res)
            dfs(root.right, sum-root.val, ls+[root.val], res)
        的方式，实际上多了很多次数据的复制
        """
        res, path = [], []  #! 注意，
        tmpSum = 0

        def help_rec(root):
            nonlocal res,path,tmpSum
            if not root:
                return
            tmpSum += root.val
            path.append(root.val)

            if not root.left and not root.right:
                if tmpSum == sum :
                    res.append(path.copy())
            else:
                help_rec(root.left)
                help_rec(root.right)
                
            path.pop()
            tmpSum-=root.val

        help_rec(root)
        return res

    """
    # iter
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        path = []
        tmpSum = 0
        nodeStack = [root]
        while len(nodeStack):
            cur = nodeStack.pop()
            path.append(cur.val)
            tmpSum += cur.val
            print(f"path is {path} and tmpSum is {tmpSum}")
            if cur.right:
                nodeStack.append(cur.right)
            if cur.left:
                nodeStack.append(cur.left)

            if tmpSum == sum:
                res.append(path)

            if not cur.right and not cur.left:
                tmp = path.pop()
                tmpSum -= val
        return res
        """
