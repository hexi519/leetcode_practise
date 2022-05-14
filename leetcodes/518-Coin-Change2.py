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
    def change(self, amount: int, coins: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.change(5,[1,2,5])
        4
        >>> s.change(3,[2])
        0
        >>> s.change(10,[10])
        1
        """
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for money in range(coin, amount + 1):
                dp[money] += dp[money - coin]
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    s.change(5, [1, 2, 5])
    # 5
    # s.change(3, [2])
    # 0
    # s.change(10, [10])
    # 1
