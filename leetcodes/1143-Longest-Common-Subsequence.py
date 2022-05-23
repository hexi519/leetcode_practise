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
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        >>> s = Solution()
        >>> s.longestCommonSubsequence("ace","abcde")
        3
        >>> s.longestCommonSubsequence("abc","abc")
        3
        >>> s.longestCommonSubsequence("abc","def")
        0
        >>> s.longestCommonSubsequence("","")
        0
        """
        if not len(text1) or not len(text2):
            return 0

        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + (0 if (i-1<0 or j-1<0) else dp[i-1][j-1] )
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])

        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    print(f"res is {sol.longestCommonSubsequence('ace','abcde')}")
    