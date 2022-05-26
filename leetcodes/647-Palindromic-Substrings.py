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

def helper(s, idxL,idxR):
    if idxL<=idxR:
        return True

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        >>> s = Solution()
        >>> s.countSubstrings("aaa")
        6
        >>> s.countSubstrings("aaaa")
        10
        >>> s.countSubstrings("abc")
        3
        >>> s.countSubstrings("abab")
        6
        """
        lenS = len(s)
        dp = [[False for _ in range(lenS+1)] for _ in range(lenS) ]

        # res = 0
        for idx in range(lenS):
            dp[idx][1],dp[idx][0] = True,True
            # res+=1
        # for leng in range(2,lenS-idx+1):
        for leng in range(2,lenS+1):
            for idx in range(lenS-leng+1):
                if s[idx]==s[idx+leng-1]:
                    dp[idx][leng] = dp[idx+1][leng-2]
                    # print(f"update dp({idx},{leng}) to be {dp[idx][leng]}, with idx+leng//2 of {idx+leng//2}")

        # print(f"dp is {dp}")
        return sum([sum(line) for line in dp]) - lenS
    
if __name__ == "__main__":
    s = Solution()
    print(f"res is {s.countSubstrings('aaaaaa')}")  # should be 21
    print(f"res is {s.countSubstrings('aaaa')}")  # should be 6
    # print(f"res is {s.countSubstrings('abab')}")
