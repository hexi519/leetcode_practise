# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard] dp
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

from sys import maxsize as MAX_INT

MIN_INT = -(MAX_INT - 1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        >>> sol = Solution()
        >>> sol.maxProfit([7,1,5,3,6,4])
        7
        >>> sol.maxProfit([3,3,5,0,0,3,1,4])
        6
        >>> sol.maxProfit([7,6,4,3,1])
        0
        >>> sol.maxProfit([1,2])
        1
        """
        day_len = len(prices)
        dp = [[MIN_INT, MIN_INT, MIN_INT, MIN_INT, MIN_INT] for _ in range(day_len)]  # 0 is no stock in hand, 1 is the opposite
        dp[0][0], dp[0][1] = 0, -prices[0]
        for day in range(1, day_len):
            dp[day][0] = 0
            dp[day][1] = max(dp[day - 1][1], dp[day - 1][0] - prices[day])
            if day >= 1:
                dp[day][2] = max(dp[day - 1][2], dp[day - 1][1] + prices[day])

            if day >= 2:
                dp[day][3] = max(dp[day - 1][3], dp[day - 1][2] - prices[day])

            if day >= 3:
                dp[day][4] = max(dp[day - 1][4], dp[day - 1][3] + prices[day])

            # print(f"dp[{day}](price {prices[day]}) is {dp[day]}")

        return max(dp[-1])


if __name__ == "__main__":
    sol = Solution()
    print(f"result is {sol.maxProfit([7, 6, 4, 3, 1])}")
