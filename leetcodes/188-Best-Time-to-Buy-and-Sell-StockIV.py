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


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        from sys import maxsize as MAX_INT
        dayLen = len(prices)
        if dayLen < 2:
            return 0
        dp = [[1 - MAX_INT for _ in range(2 * k + 1)] for _ in range(dayLen)]

        for day in range(dayLen):
            dp[day][0] = 0

        for day in range(dayLen):
            for opIdx in range(k):
                dp[day][2 * opIdx + 1] = max(dp[day - 1][2 * opIdx + 1], dp[day][2 * opIdx] - prices[day])  # k-th buy
                dp[day][2 * opIdx + 2] = max(dp[day - 1][2 * opIdx + 2], dp[day][2 * opIdx + 1] + prices[day])  # k-th buy

        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    prices = [3, 2, 6, 5, 0, 3]
    k = 0
    k = 1
    k = 2
    k = 8
    print(f"res is {sol.maxProfit(k,prices)}")
