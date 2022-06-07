# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *


class Solution:
    # binary search method -- space of O(nlogn)
    def bs_findDuplicate(self, nums):
        numRange = len(nums)
        nums.append(0)
        left, right = 0, numRange  # right是取不到的
        mid = left + (right - left) // 2

        while left < right:  # 退出条件就是left==right
            cnt = 0
            for num in nums:
                cnt += 1 if num <= mid and num >= left else 0
            if cnt > mid - left + 1:  # 这里的写法就看你寻找的是左侧边界还是右侧边界了， 但其实都一样的
                left, right = left, mid
            else:
                left, right = mid + 1, right
            mid = left + (right - left) // 2

        return left

    # fast-slow -- space of O(1):
    def findDuplicate(self, nums):
        """
        >>> s = Solution()
        >>> s.findDuplicate([1,3,4,2,2])
        2
        >>> s.findDuplicate([3,1,3,4,2])
        3
        >>> s.findDuplicate([1,3,4,2,2])
        2
        """
        slow, fast = nums[0], nums[nums[0]]  # len(nums) must be bigger than 1.
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


if __name__ == "__main__":
    sol = Solution()
    print(f"res is {sol.findDuplicate([1, 3, 4, 2, 2])}")
    print(f"res is {sol.findDuplicate([8,1,1,9,5,4,2,7,3,6])}")
