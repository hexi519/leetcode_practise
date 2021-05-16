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
        lenNum = len(nums)
        from collections import defaultdict
        ans = defaultdict(lambda:-1)
        ms = list() # mononic stack 单调递减栈 
        for idx in range(lenNum*2):
            while len(ms) and nums[ms[-1]]<nums[idx%lenNum]:
                ans[ms.pop()]= nums[idx%lenNum]
            ms.append( idx%lenNum )
        
        return [ ans[num] if ans[num]!=-1 else -1 for num in range(lenNum) ]     