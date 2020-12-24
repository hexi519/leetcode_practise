# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *

class Solution(object):
    def coinChange(self, coins, amount):
        """
        >>> s = Solution()
        >>> s.coinChange([1,2,5],11)
        3
        >>> s.coinChange([2],3)
        -1
        >>> s.coinChange([1],0)
        0
        >>> s.coinChange([1],1)
        1
        >>> s.coinChange([1],2)
        2
        """
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for coin in coins:
            for value in range(coin,amount+1):
                dp[value]=min(dp[value-coin]+1,dp[value])

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]