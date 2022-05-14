# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] dp
'''

from typing import Dict, List
from util import *


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        >>> s = Solution()
        >>> s.coinChange([1,2,5],11)
        3
        >>> s.coinChange([2],3)
        -1
        >>> s.coinChange([1],0)
        0
        """
        from sys import maxsize as MAX_INT
        dp = [MAX_INT for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for money in range(coin, amount + 1):
                dp[money] = min(dp[money - coin] + 1, dp[money])

        return dp[-1] if dp[-1] != MAX_INT else -1
