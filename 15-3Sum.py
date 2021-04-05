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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        >>> s = Solution()
        >>> s.threeSum([-1,0,1,2,-1,-4])    # [-4, -1, -1, 0, 1, 2]
        [[-1, -1, 2], [-1, 0, 1]]
        >>> s.threeSum([])
        []
        >>> s.threeSum([0])
        []
        >>> s.threeSum([0,0,0,0])
        [[0, 0, 0]]
        """
        if len(nums) < 3:
            return []
        nums.sort()

        res = []
        for cur, number in enumerate(nums[:-2]):
            l, r = cur+1, len(nums)-1
            if cur and nums[cur-1] == number:  # reduce duplicated cases
                continue
            while l < r:

                if number+nums[l]+nums[r] > 0:
                    r -= 1
                    while r and nums[r+1] == nums[r]:
                        r-=1
                elif number+nums[l]+nums[r] < 0:
                    l += 1
                    while l< len(nums)-1 and nums[l-1] == nums[l]:
                        l += 1
                else:
                    res.append([nums[cur], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l< len(nums)-1 and nums[l-1] == nums[l]:
                        l += 1
                    
                    while r and nums[r+1] == nums[r]:
                        r-=1
        return res



# 上面的更快，但是下面的这个更elegant，也就是while里面不要套while
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()

        res = []
        for cur, number in enumerate(nums):
            l, r = cur+1, len(nums)-1
            if cur and nums[cur-1] == number:  # reduce duplicated cases
                continue
            while l < r:
                if r<len(nums)-1 and nums[r+1] == nums[r]:
                    r=r-1
                    continue
                    
                if l>cur+1 and nums[l-1] == nums[l]:
                    l=l+1
                    continue
                    
                if number+nums[l]+nums[r] > 0:
                    r -= 1
                elif number+nums[l]+nums[r] < 0:
                    l += 1
                    while l+1 < len(nums) and nums[l-1] == nums[l]:
                        l += 1
                else:
                    res.append([nums[cur], nums[l], nums[r]])
                    l += 1

        return res