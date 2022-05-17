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
    def maxProfit(self, prices: List[int]) -> int:
        """
        >>> sol = Solution()
        >>> sol.maxProfit([7,1,5,3,6,4])
        7
        >>> sol.maxProfit([1,2,3,4,5])
        4
        >>> sol.maxProfit([1])
        0
        """
        day_len = len(prices)
        dp = [[0, 0] for _ in range(day_len)]  # 0 is no stock in hand, 1 is the opposite
        dp[0] = [0, -prices[0]]
        for day in range(1, day_len):
            dp[day][0] = max(dp[day - 1][0], dp[day - 1][1] + prices[day])
            dp[day][1] = max(dp[day - 1][1], dp[day - 1][0] - prices[day])

        return max(dp[-1])
