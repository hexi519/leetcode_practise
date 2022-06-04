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
    def maxProfit(self, prices: List[int], fee: int) -> int:
        lenD = len(prices)
        if lenD < 2: return 0
        from sys import maxsize as MAX_INT
        dp = [[0 - MAX_INT, 0 - MAX_INT] for _ in range(lenD)]  # 0 held, 1 not held
        dp[0] = [-prices[0], 0]

        for day in range(1, lenD):
            dp[day][1] = 0
            dp[day][0] = max(dp[day - 1][0], dp[day - 1][1] - prices[day])
            dp[day][1] = max(dp[day - 1][1], dp[day - 1][0] + prices[day] - fee)

        return max(dp[day])


if __name__ == "__main__":
    sol = Solution()
    prices, fee = [1, 3, 2, 8, 4, 9], 2  # 8
    # prices, fee = [1, 3, 7, 5, 10, 3], 3  # 6
    # prices, fee = [9, 8, 7, 1, 2], 3  # 0
    print(f"res is {sol.maxProfit(prices,fee)}")