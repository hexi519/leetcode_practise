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
    def maxPoints(self, mat: List[List[int]]) -> int:
        lenR, lenC = len(mat), len(mat[0])

        dp = [[-1000 for _ in range(lenC)] for _ in range(lenR)]
        maxAdd = [[0 for _ in range(lenC)] for _ in range(lenR)]
        maxDec = [[0 for _ in range(lenC)] for _ in range(lenR)]

        dp[0] = mat[0]
        tmpAdd, tmpDec = -1000, -1000
        for idx in range(lenC):
            if tmpAdd < dp[0][idx] + idx:
                tmpAdd = dp[0][idx] + idx

            maxAdd[0][idx] = tmpAdd

        for idx in range(lenC - 1, -1, -1):
            if tmpDec < dp[0][idx] - idx:
                tmpDec = dp[0][idx] - idx

            maxDec[0][idx] = tmpDec

        # print(f"dp[0] is {dp[0]}")
        # print(f"maxAdd[0] is {maxAdd[0]}")
        # print(f"maxDec[0] is {maxDec[0]}")

        for idxR in range(1, lenR):
            tmpAdd, tmpDec = -1000, -1000
            for idxC in range(lenC):
                dp[idxR][idxC] = maxAdd[idxR - 1][idxC] - idxC + mat[idxR][idxC]
                if idxC + 1 < lenC:
                    dp[idxR][idxC] = max(dp[idxR][idxC], maxDec[idxR - 1][idxC + 1] + idxC + mat[idxR][idxC])

                # 这边还可以加判断
                if tmpAdd < dp[idxR][idxC] + idxC:
                    tmpAdd = dp[idxR][idxC] + idxC

                maxAdd[idxR][idxC] = tmpAdd

            for idxC in range(lenC - 1, -1, -1):
                if tmpDec < dp[idxR][idxC] - idxC:
                    tmpDec = dp[idxR][idxC] - idxC

                maxDec[idxR][idxC] = tmpDec

            # print(f"idxR is {idxR}:")
            # print(f"\tupdate dp to be {dp[idxR]}")
            # print(f"\tupdate maxAdd to be {maxAdd[idxR]}")
            # print(f"\tupdate maxDec to be {maxDec[idxR]}")

        return max(dp[-1])


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]  # 9
    mat = [[1, 5], [2, 3], [4, 2]]  # 11
    # mat = [[0, 3, 0, 4, 2], [5, 4, 2, 4, 1], [5, 0, 0, 5, 1], [2, 0, 1, 0, 3]]  # 15
    print(f"res is {sol.maxPoints(mat)}")
