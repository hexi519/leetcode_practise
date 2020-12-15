# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *

from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        """
        >>> s = Solution()
        >>> s.numSquares(12)
        3
        >>> s.numSquares(13)
        2
        >>> s.numSquares(0)
        0
        """
        # digitList = []
        ans = [n] * (n + 1)
        for i in range(n + 1):
            ans[i] = i

        for digit in range(1, n + 1):
            if int(sqrt(digit)) * int(sqrt(digit)) != digit:
                # print(f"drop digit {digit}")
                continue
            # digitList.append(digit)
            # print(f"choose digit {digit}:")
            for num in range(digit, 1 + n):  # 多重背包
                # print(f"\tupdate ans[{num}]=min({ans[num]},ans[{num-digit}]={ans[num-digit]} +1)")
                ans[num] = min(ans[num], ans[num - digit] + 1)  # not choose ,choose

        return ans[n]