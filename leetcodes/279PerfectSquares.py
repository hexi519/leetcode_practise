# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *

from math import sqrt
"""
# solution 1: dp
class Solution:
    def numSquares(self, n: int) -> int:
        # >>> s = Solution()
        # >>> s.numSquares(12)
        # 3
        # >>> s.numSquares(13)
        # 2
        # >>> s.numSquares(0)
        # 0
        
        # 打表
        squares = []
        for i in range(1, int(n**0.5) + 1):
            squares.append(i**2)

        from sys import maxsize as MAX_INT
        dp = [MAX_INT for _ in range(n + 1)]
        dp[0] = 0
        for square in squares:
            if square > n:
                break
            for digit in range(square, n + 1):
                dp[digit] = min(dp[digit], dp[digit - square] + 1)

        return dp[-1]
"""


# solution 2: bfs 快很多
class Solution:
    def numSquares(self, n: int) -> int:
        """
        >>> s = Solution()
        >>> s.numSquares(12)
        3
        >>> s.numSquares(13)
        2
        >>> s.numSquares(1)
        1
        >>> s.numSquares(7)
        4
        """
        from collections import deque

        numbers = set()
        q = set()
        for i in range(1, n + 1):
            if int(i**0.5)**2 == i:
                numbers.add(i)

        # print(f"numbers is {numbers}")

        q.add(n)
        lev = 1
        while len(q):
            tmp = set()  #* 没有别的地方可以优化了，bfs比较难优化，dfs还可以记忆化，但是bfs就这样了...
            for cur in q:
                if cur in numbers:
                    # print(f"cur {cur} in numbers")
                    return lev
                [tmp.add(cur - num) for num in numbers if cur > num]
            lev += 1
            q = tmp