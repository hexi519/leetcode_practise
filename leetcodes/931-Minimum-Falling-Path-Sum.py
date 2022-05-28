# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] dp
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        leng = len(matrix)
        dp = [[11000 for _ in range(leng + 2)] for _ in range(leng + 2)]

        for idx in range(1, leng + 1):
            dp[0][idx] = 0

        for idxR in range(1, leng + 1):
            for idxC in range(1, leng + 1):
                dp[idxR][idxC] = min(dp[idxR - 1][idxC - 1], dp[idxR - 1][idxC], dp[idxR - 1][idxC + 1]) + matrix[idxR - 1][idxC - 1]

            print(f"update row {idxR} to be {dp[idxR]}")

        return min(dp[-2][1:-1])


if __name__ == '__main__':
    sol = Solution()
    mat = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    # mat = [[-48]]
    print(f"res is {sol.minFallingPathSum(mat)}")
