# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[right if right < len(nums) else -1] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


if __name__ == '__main__':
    sol = Solution()
    print(f"res is {sol.findMin([3, 4, 5, 1, 2])}")  # 1
    print(f"res is {sol.findMin([2, 3, 4, 5, 1])}")  # 1
    print(f"res is {sol.findMin([1, 2, 3, 4, 5])}")  # 1
