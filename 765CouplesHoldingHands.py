# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *

class Solution:
    def minSwapsCouples(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.minSwapsCouples([0, 2, 1, 3])
        1
        >>> s.minSwapsCouples([3, 2, 0, 1])
        0
        >>> s.minSwapsCouples([2,0,5,4,3,1])
        1
        """
        # helper array
        value2idx =[0]*len(nums)
        for (idx, num) in enumerate(nums):
            value2idx[num] = idx
        
        res = 0
        for idx in range(0, len(nums),2 ):
            if nums[idx]//2 == nums[idx+1]//2:
                continue
            couple = nums[idx]+1 if nums[idx]%2==0 else nums[idx]-1
            nums[idx+1] , nums[value2idx[couple]] = nums[value2idx[couple]] ,nums[idx+1]
            value2idx[nums[value2idx[couple]]] = value2idx[couple]
            res+=1

        return res