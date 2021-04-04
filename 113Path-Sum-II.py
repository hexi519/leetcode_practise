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

    # iterasive 
    #! 心得：别看iterasive似乎很多空间，但其实recursive更多！(牵扯到很多数据的copy...此外还有栈开销...)
    # 一开始没写出来iterasive的，没有往栈里面记录信息，所以很多信息在节点中无法传递
    def pathSum(self, root, s): 
        if not root:
            return []
        res = []
        #* 因为有时候从一个节点到另一个节点，路径会突变，所以栈里面把路径信息也放进去
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls+[curr.left.val]))
        return res