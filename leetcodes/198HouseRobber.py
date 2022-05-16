# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy] dp 
'''

from typing import Dict, List
from util import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.rob([1,2,3,1])
        4
        >>> s.rob([2,7,9,3,1])
        12
        """
        if len(nums) < 2:
            return max(nums)
        """
        dp = [[0, 0] for _ in range(len(nums))]

        dp[0][1], dp[1][0] = nums[0], nums[0]
        dp[1][1] = nums[1]
        for i in range(2, len(nums)):
            dp[i][0] = max(dp[i - 1])
            dp[i][1] = max(dp[i - 1][0], max(dp[i - 2])) + nums[i]

        # print(f"dp is {dp}")
        return max(dp[-1])
        """
        # 滚动数组的做法
        """
        dp = dict()
        dp['before'], dp['last'], dp['cur'] = [0, 0], [0, 0], [0, 0]
        dp['before'][1], dp['last'][0] = nums[0], nums[0]
        dp['last'][1] = nums[1]

        for i in range(2, len(nums)):
            dp['cur'][0] = max(dp['last'])
            dp['cur'][1] = max(dp['last'][0], max(dp['before'])) + nums[i]
            dp['before'], dp['last'] = dp['last'].copy(), dp['cur'].copy()

        return max(dp['last'])
        """
        """
        # dp = [0 for _ in range(nums)]
        dp = [[0, 0] for _ in range(len(nums))]

        dp[0][1], dp[1][0] = nums[0], nums[0]
        dp[1][1] = nums[1]
        for j in range(2, len(nums)):
            dp[j][0] = max(dp[j - 1])
            dp[j][1] = dp[j - 1][0] + nums[j]

        return max(dp[-1])
        """
        dp = [0 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
