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
        lenD = len(prices)
        dp = [[0 for _ in range(3)] for _ in range(lenD)]  # state：1 -- stock held; 2 -- stack sold; 0 -- no trade or cool down

        dp[0][1] = -prices[0]
        for day in range(1, lenD):
            dp[day][1] = max(dp[day - 1][1], dp[day - 1][0] - prices[day])
            dp[day][2] = dp[day - 1][1] + prices[day]
            dp[day][0] = max(dp[day - 1][2], dp[day - 1][0])

        return max(dp[-1])


if __name__ == "__main__":
    sol = Solution()
    prices = [1, 2, 3, 0, 2]  # 3
    prices = [1]  # 0
    print(f"res is {sol.maxProfit(prices)}")
