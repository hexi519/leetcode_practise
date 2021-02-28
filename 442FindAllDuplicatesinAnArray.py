# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        >>> s = Solution()
        >>> s.findDuplicates([4,3,2,7,8,2,3,1])
        [2, 3]
        """
        numsLen = len(nums)+1
        nums.append(0)  # for convenience
        
        for (idx, num) in enumerate(nums):
            nums[num%numsLen]+= numsLen 

        res = [idx  for (idx, num) in enumerate(nums)  if num//numsLen>1 ]

        return res
