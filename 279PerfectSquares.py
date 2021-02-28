<<<<<<< HEAD
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
        ans = [n] * (n + 1)
        ans[0]=0

        # 其实这样初始化也可以（简洁且方便
        # for i in range(n + 1): ans[i] = i

        for digit in range(1, n + 1):
            if int(sqrt(digit)) * int(sqrt(digit)) != digit:
                continue
            for num in range(digit, 1 + n):  # 多重背包
                ans[num] = min(ans[num], ans[num - digit] + 1)  # not choose ,choose

        return ans[n]
"""


# solution 2: bfs
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
=======
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
        ans = [n] * (n + 1)
        ans[0]=0

        # 其实这样初始化也可以（简洁且方便
        # for i in range(n + 1): ans[i] = i

        for digit in range(1, n + 1):
            if int(sqrt(digit)) * int(sqrt(digit)) != digit:
                continue
            for num in range(digit, 1 + n):  # 多重背包
                ans[num] = min(ans[num], ans[num - digit] + 1)  # not choose ,choose

        return ans[n]
"""
# solution 2: bfs
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
                [tmp.add(cur - num )for num in numbers if cur > num]
            lev += 1
>>>>>>> hesy/master
            q = tmp