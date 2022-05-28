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
    def longestPalindrome(self, s: str) -> str:
        """
        >>> s = Solution()
        >>> s.longestPalindrome('babad')
        'bab'
        >>> s.longestPalindrome('b')
        'b'
        >>> s.longestPalindrome('cccdddd')
        'dddd'
        >>> s.longestPalindrome('abcdbbfcba')
        'bb'
        """
        leng = len(s)
        dp = [[False for _ in range(leng)] for _ in range(leng)]
        for idxS in range(leng):
            dp[idxS][idxS] = True

        resIdx, resL = 0, 0
        for l in range(1, leng):
            for idxS in range(leng):
                if idxS + l >= leng:
                    break
                if s[idxS] == s[idxS + l]:
                    if l == 1 or dp[idxS + 1][idxS + l - 1]:
                        dp[idxS][idxS + l] = True
                        if l > resL:
                            resL = l
                            resIdx = idxS

        return s[resIdx:resIdx + 1 + resL]
        """
        leng = len(s)
        if leng < 2:
            return s

        dp = [[False for _ in range(leng + 1)] for _ in range(leng)]

        for idx in range(leng):
            dp[idx][0], dp[idx][1] = True, True

        resLen, resIdx = 1, 0
        for l in range(2, leng + 1):
            for idx in range(leng + 1 - l):
                if s[idx] == s[idx + l - 1]:
                    if dp[idx + 1][l - 2]:
                        dp[idx][l] = dp[idx + 1][l - 2]
                        if l > resLen:
                            resLen = l
                            resIdx = idx
            # print(f"len is {l}, dp is {dp}")

        return s[resIdx:resIdx + resLen]

        """


if __name__ == "__main__":
    s = Solution()
    print(f"res is {s.longestPalindrome('abcdbbfcba')}")
