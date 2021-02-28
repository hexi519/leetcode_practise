<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        >>> s = Solution()
        >>> s.canPartition([1,5,11,5])
        True
        >>> s.canPartition([1,2,3,5])
        False
        """
        if not len(nums): return False
        goal = sum(nums)
        if goal % 2: return False
        half = goal // 2
        # initialization
        dp = [False] * (half + 1)
        dp[0]=True

        for digit in range(len(nums)):  # for i-th thing
            if nums[digit] > half: continue
            for value in range(half, nums[digit] - 1, -1):
                dp[value] |= dp[value - nums[digit]]
            # print(f"after {digit}-th({nums[digit]}) update, dp is {dp}")

        return dp[-1]
=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        >>> s = Solution()
        >>> s.canPartition([1,5,11,5])
        True
        >>> s.canPartition([1,2,3,5])
        False
        """
        if not len(nums): return False
        goal = sum(nums)
        if goal % 2: return False
        half = goal // 2
        # initialization
        dp = [False] * (half + 1)
        dp[0]=True

        for digit in range(len(nums)):  # for i-th thing
            if nums[digit] > half: continue
            for value in range(half, nums[digit] - 1, -1):
                dp[value] |= dp[value - nums[digit]]
            # print(f"after {digit}-th({nums[digit]}) update, dp is {dp}")

        return dp[-1]
>>>>>>> hesy/master
