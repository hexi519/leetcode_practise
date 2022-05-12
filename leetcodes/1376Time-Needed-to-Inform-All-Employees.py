# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log


# from bottom to up
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.numOfMinutes(15,0,[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6],[ 1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
        3
        >>> s.numOfMinutes( 1, 0, [-1], [0,0,1,0,0,0])
        0
        >>> s.numOfMinutes( 6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0])
        1
        """
        # time from cur to root
        timeAll = [None]*n
        for idx,man in enumerate(manager):
            if timeAll[idx]!=None :continue
            tmpTime = 0 
            while man!=-1:  # 直到
                tmpTime +=informTime[man]
                if timeAll[man]!=None:
                    tmpTime += timeAll[man]
                    break
                man = manager[man]
            
            timeAll[idx] = tmpTime # if timeAll[idx] else 
        
        return max(timeAll) if n!=1 else 0
