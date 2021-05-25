# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

#TODO 回溯和dp都要做一遍，其中回溯和递归都看下，哪个复杂度更低(分别对应  和 str+'(' 的方式)
# 讲道理，效果上应该是 dp>回溯>递归

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        >>> sol = Solution()
        >>> sol.removeInvalidParentheses(")(")
        ['']
        """
        leftRemove, rightRemove = 0, 0
        for char in s:
            if char == '(':
                leftRemove += 1
            elif char == ')':
                if leftRemove > 0:
                    leftRemove -= 1
                else:
                    rightRemove += 1
        log.info(f"leftRemove,rightRemove is {leftRemove},{rightRemove}")

        res = set()
        def dfs(idx, leftCount, rightCount, leftRemove, rightRemove, strs):
            if idx == len(s):
                if not leftRemove and not rightRemove:
                    res.add(strs)
                return
            if s[idx] == '(' and leftRemove:
                dfs(idx+1, leftCount, rightCount, leftRemove-1, rightRemove, strs)
            if s[idx] == ')' and rightRemove:
                dfs(idx+1, leftCount, rightCount, leftRemove, rightRemove-1, strs)
            if s[idx] not in '()':
                dfs(idx+1, leftCount, rightCount, leftRemove, rightRemove, strs+s[idx])
            elif s[idx] == '(':
                dfs(idx+1, leftCount+1, rightCount, leftRemove, rightRemove, strs+s[idx])
            elif rightCount < leftCount:
                dfs(idx+1, leftCount, rightCount+1, leftRemove, rightRemove, strs+s[idx])
            return
        dfs(0, 0, 0, leftRemove, rightRemove, '')
        return list(res)