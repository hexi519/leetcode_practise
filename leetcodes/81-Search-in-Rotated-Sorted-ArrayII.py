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

    def search(self, nums, target):
        """
        >>> s = Solution()
        >>> s.search([3,1],3)
        0
        """
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return True

            # if nums[low] == nums[mid] and nums[mid] == nums[high if high < len(nums) else -1]:
            if nums[low] == nums[mid]:
                low += 1

            elif nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                upper = nums[high - 1] if high == len(nums) else nums[high]
                if nums[mid] < target <= upper:
                    low = mid + 1
                else:
                    high = mid

        return False


if __name__ == "__main__":
    sol = Solution()
    # print(f"res is {sol.search([2,5,6,0,0,1,2],0)}")  # true
    # print(f"res is {sol.search([2,5,6,0,0,1,2],3)}")  # false
    # print(f"res is {sol.search([1,1,1,1],3)}")  # false
    # print(f"res is {sol.search([1,1,1,3],3)}")  # true
    # print(f"res is {sol.search([3,1,1,1],3)}")  # true
    # print(f"res is {sol.search([1,0,1,1,1],0)}")  # true
    # print(f"res is {sol.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],2)}")  # true
    print(f"res is {sol.search([2,2,2,0,1],0)}")  # true
