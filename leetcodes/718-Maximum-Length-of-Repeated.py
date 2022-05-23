# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] dp
'''

from typing import Dict, List
from util import *
# from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.findLength([1,2,3,2,1],[3,2,1,4,7])
        3
        >>> s.findLength([0,0,0,0,0],[0,0,0,0,0])
        5
        >>> s.findLength([0,0,0,0,0],[1,1,1,1,1])
        0
        """
        res = 0
        dp = [ [0 for _ in range(len(nums2))] for _ in range(len(nums1))]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    dp[i][j] = 1 + (0 if (i-1<0 or j-1<0) else dp[i-1][j-1] )
                res = max(res,dp[i][j])
            
            # print(f"dp is {dp}")

        return res

if __name__ == "__main__":
    s = Solution()
    print(f"res is {s.findLength([1,2,3,2,1],[3,2,1,4,7])}")

        
