# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

# ipdb.set_trace = blockIpdb
blockPrint()
enablePrint()


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.minSubArrayLen(15,[2,14])
        2
        >>> s.minSubArrayLen(7,[2,3,1,2,4,3])
        2
        >>> s.minSubArrayLen(4,[1,4,4])
        1
        >>> s.minSubArrayLen(11,[1,1,1,1,1,1,1,1])
        0
        """
        curSum,ans = 0,len(nums) + 1
        s, f = 0, 0
        while f < len(nums):
            # 加上
            curSum += nums[f]
            f += 1

            # s前移
            while curSum >= target and s < len(nums):
                ans = min(ans, f - s)
                curSum -= nums[s]
                s += 1

        return 0 if ans == len(nums) + 1 else ans
