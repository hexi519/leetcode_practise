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
    def findMin(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.findMin([2,1])
        1
        >>> s.findMin([2,5,6,0,1])
        0
        >>> s.findMin([1])
        1
        """
        if not nums:
            return -1
        low, high = 0, len(nums)-1  #!这里要采用左闭右闭的形式是因为，如果 nums[mid] < nums[low]判断过后，不能直接扔掉nums[mid]，因为也许他就是最小值。
        while low < high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:   # 一种情况是
                # if nums[low] < nums[high]:
                #     return nums[low]
                # else:
                    low = mid + 1
            else:
                high = mid
        return nums[low]


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set left and right bounds
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid
        return nums[left]
