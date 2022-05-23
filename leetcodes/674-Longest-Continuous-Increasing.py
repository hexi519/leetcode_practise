# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy] dp
'''

from typing import Dict, List
from util import *
# from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.findLengthOfLCIS([1,3,5,4,7])
        3
        >>> s.findLengthOfLCIS([2,2,2,2,2])
        1
        >>> s.findLengthOfLCIS([0])
        1
        """
        dp = [1 for _ in  range(len(nums))]
        res = 1
        for idx in range(1,len(nums)):
            if nums[idx]>nums[idx-1]:
                dp[idx] = dp[idx-1]+1
            
            res = max(res,dp[idx])

        return res