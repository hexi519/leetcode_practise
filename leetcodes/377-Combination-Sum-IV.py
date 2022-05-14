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
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        >>> s = Solution()
        >>> s.combinationSum4([9],3)
        0
        >>> s.combinationSum4([1,2,3],4)
        7
        """
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for money in range(1, target + 1):
            for coin in nums:
                if money >= coin:
                    dp[money] += dp[money - coin]

        return dp[-1]
