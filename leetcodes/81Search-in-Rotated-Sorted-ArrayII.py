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
    def search(self, nums, target):
        """
        >>> s = Solution()
        >>> s.search([2,5,6,0,0,1,2],0)
        True
        >>> s.search([2,5,6,0,0,1,2],3)
        False
        >>> s.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],2)
        True
        >>> s.search([1],0)
        False
        """
        if not nums:
            return -1
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return True

            if nums[low] == nums[mid]:  # 存在11011 或者11211 这种干扰项，只要将前半部分重复的去掉，就能还原成33的情况。这里为什么每次+1而不是用while --》 1. 代码优雅 2. 不易出错
                low += 1

            elif nums[low] < nums[mid]:
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

        return True if nums[low-1] == target else False
