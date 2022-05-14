# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] dp
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def integerBreak(self, n: int) -> int:
        """
        >>> s = Solution()
        >>> s.integerBreak(2)
        1
        >>> s.integerBreak(10)
        36
        """
        if n == 2:
            return 1

        dp = [i - 1 for i in range(n + 1)]
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i // 2 + 1):
                #* 左半部分可以不用拆了，max(j,dp[j])-->j，因为拆的情况在从左向右遍历的时候已经考虑入内了
                dp[i] = max(j * max(dp[i - j], i - j), dp[i])

        return dp[-1]