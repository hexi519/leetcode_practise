# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy] monotone stack
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        >>> s = Solution()
        >>> s.nextGreaterElement([4,1,2],[1,3,4,2])
        [-1, 3, -1]
        >>> s.nextGreaterElement([2,4],[1,2,3,4])
        [3, -1]
        """
        from collections import defaultdict
        ans = defaultdict(lambda:-1)
        ms = list() # mononic stack 单调递减栈 
        for num in nums2:
            while len(ms) and ms[-1]<num:
                ans[ms.pop()]=num
            ms.append(num)
        
        return [ ans[num] for num in nums1 ]            
