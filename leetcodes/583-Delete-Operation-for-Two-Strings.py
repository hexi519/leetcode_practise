# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
# from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        >>> s = Solution()
        >>> s.minDistance("sea","eat")
        2
        >>> s.minDistance("acde","ced")
        3
        >>> s.minDistance("","")
        0
        """
        len1,len2 = len(word1)+1,len(word2)+1
        dp = [[0 for _ in range(len2)] for _ in range(len1)]

        for idx1 in range(1,len1):
            dp[idx1][0] = idx1
        
        for idx2 in range(1,len2):
            dp[0][idx2] = idx2
        
        for idx1 in range(1,len1):
            for idx2 in range(1,len2):
                if word1[idx1-1] == word2[idx2-1]:
                    dp[idx1][idx2] = dp[idx1-1][idx2-1]
                else: 
                    dp[idx1][idx2] = min(dp[idx1-1][idx2],dp[idx1][idx2-1])+1
            
        return dp[-1][-1]
