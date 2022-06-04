# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard] dp
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        if k == 1:
            return n

        from sys import maxsize as MAX_INT
        dp = [[MAX_INT for _ in range(n + 1)] for _ in range(k + 1)]

        dp[1] = [floor for floor in range(n + 1)]

        for egg in range(2, k + 1):
            dp[egg][0] = 0
            # dp[egg][1] = 1
            for allF in range(1, n + 1):
                # for floor in range(1, allF):
                # print(f"\tallF {allF}, dp[{egg}][{allF}] is {dp[egg][allF]}")
                for floor in range(allF, 0, -1):
                    dp[egg][allF] = min(dp[egg][allF], 1 + max(dp[egg - 1][floor - 1], dp[egg][allF - floor]))
                    # print(f"\t\tfloor {floor}, dp[{egg}][{allF}] is {dp[egg][allF]}, with {dp[egg - 1][floor - 1]},{dp[egg][allF - floor]}")

            # print(f"dp[{egg}] is {dp[egg]}")
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    k, n = 1, 2
    # k, n = 2, 6  # 3
    # print(f"res is {sol.superEggDrop(k, n)}")
    k, n = 3, 14  # 4
    print(f"res is {sol.superEggDrop(k, n)}")
