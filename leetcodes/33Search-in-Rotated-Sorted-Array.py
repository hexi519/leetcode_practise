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
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        """
        >>> s = Solution()
        >>> s.search([3,1],3)
        0
        """
        if not nums:
            return -1
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                upper = nums[high-1] if high == len(nums) else nums[high]
                if nums[mid] < target <= upper:
                    low = mid + 1
                else:
                    high = mid

        return low if nums[low-1] == target else -1
