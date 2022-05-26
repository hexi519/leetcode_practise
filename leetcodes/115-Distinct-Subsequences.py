# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *
# from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        >>> sol = Solution()
        >>> sol.numDistinct("rabbbit","rabbit")
        3
        >>> sol.numDistinct("babag","bag")
        3
        >>> sol.numDistinct("babgbag","bag")
        5
        >>> sol.numDistinct("b","c")
        0
        """
        lenS ,lenT = len(s)+1,len(t)+1
        if lenS<lenT:
            return 0
        
        dp = [[0 for _ in range(lenT)] for _ in range(lenS)] 
        for idx in range(lenS):
            dp[idx][0]=1

        for idxS in range(1,lenS):
            for idxT in range(1,lenT):
                if s[idxS-1] == t[idxT-1]:
                    dp[idxS][idxT] = dp[idxS-1][idxT-1]+dp[idxS-1][idxT]
                else:
                    dp[idxS][idxT] = dp[idxS-1][idxT]
        # print(f"dp is {dp}")
        return dp[-1][-1]

if __name__ == "__main__":
    sol = Solution()
    # sol.numDistinct("rabbbit","rabbit")
    # print(f"res is {sol.numDistinct('babag','bag')}")
    print(f"res is {sol.numDistinct('babgbag','bag')}")
       