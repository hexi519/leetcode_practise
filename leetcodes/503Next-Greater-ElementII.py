# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   []
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        >>> s = Solution()
        >>> s.nextGreaterElements([1,2,1])
        [2, -1, 2]
        >>> s.nextGreaterElements([1,2,3,4,3])
        [2, 3, 4, -1, 4]
        """
        idx = 0
        lenNums = len(nums)
        stack,res=[],[-1 for _ in range(lenNums)]
        while idx < 2*lenNums: #and popNum<=lenNums :
            while len(stack) and nums[stack[-1]]<nums[idx%lenNums]:
                res[stack.pop()] = nums[idx%lenNums]

            stack.append(idx%lenNums)
            idx+=1
        
        return res   