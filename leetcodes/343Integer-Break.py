# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution(object):
    def integerBreak(self, n):
        """
        >>> s = Solution()
        >>> s.integerBreak(10)
        36
        >>> s.integerBreak(3)
        2
        """
        dp = [i-1 for i in range(n+1) ]
        dp[1]=1
        # dp[1], dp[2] = 1, 1
        for num in range(1, n+1):
            for number in range(1, num):
                # dp[num] = max(dp[num], max(dp[number], number)* max(dp[num-number], num-number))
                dp[num] = max(dp[num], number* max(dp[num-number], num-number))  # 左半部分的number就没必要拆了，不然就重复了

        return max(dp[1:])
