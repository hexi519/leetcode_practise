# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        >>> s = Solution()
        >>> s.minDistance("horse","ros")
        3
        >>> s.minDistance("intention","execution")
        5
        >>> s.minDistance("","")
        0
        """
        len1,len2 = len(word1),len(word2) 
        if not len1 :return len2
        if not len2 :return len1

        dp = [ [0]*(len2+1) for _ in range(len1+1) ]
        for i in range(1,len1+1):
            dp[i][0] = i #ord(word1[i-1]) + dp[i-1][0]
        for j in range(1,len2+1):
            dp[0][j] = j #ord(word2[j-1]) + dp[0][j-1]

        for i in range(len1):
            for j in range(len2):
                dp[i+1][j+1] = dp[i][j] if word1[i]==word2[j] else min(dp[i][j+1],dp[i+1][j],dp[i][j])+1
        
        # print(dp)
        return dp[-1][-1]