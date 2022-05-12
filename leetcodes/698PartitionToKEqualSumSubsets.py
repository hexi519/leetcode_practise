# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *

import numpy as np

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        >>> s = Solution()
        >>> s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1]，4)
        True
        >>> s.canPartitionKSubsets([4, 3, 2, 3, 5, 2]，4)
        False
        """
        if len(nums)<k or not k : return False
        sum_ = sum(nums)
        if sum_%k : return False
        part = sum_//k
 
        mark = [False]*len(nums)
        # dp = [False] * (part + 1)
        for times in range(1,k):
            dp = [False] * (part + 1)
            dp[0]=True

            for digit in range(len(nums)):  # for i-th thing
                if mark[digit] or nums[digit] > part: continue
                if dp[-1]: break
                for value in range(part, nums[digit] - 1, -1):
                    dp[value] |= dp[value - nums[digit]]
                print(f"k,dp is {times},{dp}")
                print(f"mark is {mark},{dp}")

            if not dp[-1]:  return False
        
        return sum( np.array(nums)[mark] )==part
            