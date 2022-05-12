# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy]
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution(object):
    def mySqrt(self, x):
        """
        >>> s = Solution()
        >>> s.mySqrt(6)
        2
        >>> s.mySqrt(4)
        2
        >>> s.mySqrt(9)
        3
        """
        l ,r = 0, x//2+2
        if x ==0 : return 0
        while l < r:
            mid = (l+r)//2
            if mid**2 < x:
                l = mid+1
                # log.info(f"l,mid,r is ,{l},{mid},{r} and moves left to {}")
            elif mid**2 > x:
                r = mid # 找左边界
            else:   # mid**2==x
                return mid
        
        return l-1