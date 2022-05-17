# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy] dp
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

from sys import maxsize as MAX_INT


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        >>> sol = Solution()
        >>> sol.maxProfit([7,1,5,3,6,4])
        5
        >>> sol.maxProfit([7,6,4,3,1])
        0
        >>> sol.maxProfit([0])
        0
        """
        minVal = MAX_INT
        maxRes = 0
        for d in range(len(prices)):
            maxRes = max(maxRes, prices[d] - minVal)
            # print(f"prices[{d}]({prices[d]}): minVal is {minVal}, maxRes is {maxRes}")
            minVal = min(minVal, prices[d])

        return maxRes
