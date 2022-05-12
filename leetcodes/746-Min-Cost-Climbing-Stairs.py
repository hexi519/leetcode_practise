# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy]
'''

from cmath import cos
from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.minCostClimbingStairs([10,15,20])
        15
        >>> s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
        6
        """
        num_stair = len(cost)
        if num_stair<2: 
            return cost[-1]

        res = [0 for _ in range(num_stair+1)]
        res[0],res[1] = cost[0],cost[1]
        for i in range(2,num_stair):
            res[i] = min(res[i-1],res[i-2])+cost[i]
        
        return min(res[-2],res[-3])
