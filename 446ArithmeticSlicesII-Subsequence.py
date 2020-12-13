# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *

import collections

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.numberOfArithmeticSlices([2, 4, 6, 8, 10])
        7
        >>> s.numberOfArithmeticSlices([7,7,7,7])
        3
        >>> s.numberOfArithmeticSlices([-1,-2,-3,-4,-5])
        7
        >>> s.numberOfArithmeticSlices([2,2,3,4])
        2
        >>> s.numberOfArithmeticSlices([])
        0
        """
        size = len(A)
        if len(A) < 3 or not A : return 0    
        ans = 0
        dp = [collections.defaultdict(int) for x in range(size)]
        for x in range(size):
            for y in range(x):
                delta = A[x] - A[y]
                # 为下次做准备，如果有连续的，也是要在之前连续的
                dp[x][delta] += 1
                # 如果有连续的，那么就是之前连续的基础上再+1,但是此时上面已经加过1了，所以就不用加了
                if delta in dp[y]:
                    dp[x][delta] += dp[y][delta]
                    ans += dp[y][delta] # 个人感觉，dp[i][j]当前的值，是为了后续的summarization做准备的
        return ans
