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
    def numTrees(self, n: int) -> int:
        """
        >>> s = Solution()
        >>> s.numTrees(3)
        5
        >>> s.numTrees(1)
        1
        >>> s.numTrees(4)
        14
        """

        dp = [1 for _ in range(n + 1)]  # is 0 a must?

        for i in range(1, n + 1):
            tmpSum = 0
            for j in range(1, i + 1):
                tmpSum += dp[j - 1] * dp[i - j]

            dp[i] = tmpSum

        # print(f"dp is {dp}")
        return dp[-1]
