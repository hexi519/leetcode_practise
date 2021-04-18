# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy]
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution(object):
    def maxSubArray(self, nums):
        """
        >>> s = Solution()
        >>> s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> s.maxSubArray([1])
        1
        >>> s.maxSubArray([5,4,-1,7,8])
        23
        """
        dp = [None]*len(nums)
        for idx, number in enumerate(nums):
            if idx == 0:
                dp[idx] = number
                # log.info(f"idx == 0,dp is {dp}")
            else:
                dp[idx] = number + (dp[idx-1] if dp[idx-1] > 0 else 0)
                # log.info(f"idx != 0,,number is {number}, and dp is {dp}")
        
        # log.info(f"dp is {dp}")
        return max(dp)
