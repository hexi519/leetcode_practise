# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution:
    """
    >>> s = Solution()
    >>> s.productExceptSelf([1,2,3,4])
    [24, 12, 8, 6]
    >>> s.productExceptSelf([-1,1,0,-3,3])
    [0, 0, 9, 0, 0]
    >>> s.productExceptSelf([-1,1])
    [1, -1]
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sequence = nums
        rever = nums[::-1]
        ans = [None]*len(sequence)
        for i in range(1, len(sequence)):
            sequence[i] *= sequence[i-1]
            rever[i] *= rever[i-1]

        rever.reverse()
        for i in range(len(sequence)):
            if i-1 < 0:
                ans[i] = rever[i+1]
            elif i+1 >= len(nums):
                ans[i] = sequence[i-1]
            else:
                ans[i] = sequence[i-1]*rever[i+1]

        # log.info(f"sequence is {sequence}")
        # log.info(f"rever is {rever}")
        # ans[0] = rever[len(nums)-0-2]
        return ans
