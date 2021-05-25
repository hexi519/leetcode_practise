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
    def maxArea(self, height: List[int]) -> int:
        """
        >>> sol = Solution()
        >>> sol.maxArea([1,8,6,2,5,4,8,3,7])
        49
        >>> sol.maxArea([1,1])
        1
        >>> sol.maxArea([4,3,2,1,4])
        16
        >>> sol.maxArea([1,2,1])
        2
        """
        l,r=0,len(height)-1
        res = 0
        while l<r:
            if height[l]<height[r]:
                res=max(res,(r-l)*height[l])
                l+=1
            else:
                res=max(res,(r-l)*height[r])
                r-=1
        
        return res


