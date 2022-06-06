# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] bs
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


def getIdx(idx, colNum):
    rowIdx = idx // colNum
    colIdx = idx % colNum
    return rowIdx, colIdx


class Solution:

    #* shorter with nice use of bisect
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])

        def get(idx: int) -> int:
            r, c = divmod(idx, n)
            return matrix[r][c]

        from bisect import bisect_left
        return get(bisect_left(range(len(matrix) * n - 1), target, key=get)) == target

    def hesy_searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False


if __name__ == "__main__":
    sol = Solution()
    m, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3
    print(f"res is {sol.searchMatrix(m,target)}")
    m, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13  # only false
    print(f"res is {sol.searchMatrix(m,target)}")
    m, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1
    print(f"res is {sol.searchMatrix(m,target)}")
    m, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60
    print(f"res is {sol.searchMatrix(m,target)}")
