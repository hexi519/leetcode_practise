<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] 
'''

from typing import Dict, List
from util import *
import numpy as np


class Solution:
    # TODO 时空复杂度也很差.空间我能理解，要滚动数组优化一下。时间为啥这么差...
    """
        Runtime: 128 ms, faster than 5.85% of Python3 online submissions for Unique Paths II.
        Memory Usage: 31 MB, less than 5.25% of Python3 online submissions for Unique Paths II.
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        >>> s = Solution()
        >>> s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
        2
        >>> s.uniquePathsWithObstacles([[0,1],[0,0]])
        1
        >>> s.uniquePathsWithObstacles([[1,0]])
        0
        >>> s.uniquePathsWithObstacles([[1],[0]])
        0
        """
        rowNum, colNum = len(obstacleGrid), len(obstacleGrid[0])
        if (obstacleGrid[-1][-1] == 1): return 0
        if (rowNum == colNum and rowNum == 1): return 1
        sol = np.array([[0] * colNum for _ in range(rowNum)])

        sol[0] = 1
        sol[:, 0] = 1

        for rowIdx, row in enumerate(obstacleGrid):
            for colIdx, col in enumerate(row):
                if col == 1:
                    if colIdx == 0:
                        # sol[rowIdx:][colIdx] = -1     # TODO 这样写就是不行...索引...
                        sol[rowIdx:, colIdx] = -1
                    if rowIdx == 0:
                        sol[rowIdx, colIdx:] = -1

                    sol[rowIdx][colIdx] = -1

        # print(f"sol is {sol}")

        for row in range(1, rowNum):
            for col in range(1, colNum):
                if (sol[row][col] == -1): continue
                sol[row][col] += sol[row][col - 1] if sol[row][col - 1] != -1 else 0
                sol[row][col] += sol[row - 1][col] if sol[row - 1][col] != -1 else 0

        return sol[-1][-1] if sol[-1][-1] != -1 else 0
=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] 
'''

from typing import Dict, List
from util import *
import numpy as np


class Solution:
    # TODO 时空复杂度也很差.空间我能理解，要滚动数组优化一下。时间为啥这么差...
    """
        Runtime: 128 ms, faster than 5.85% of Python3 online submissions for Unique Paths II.
        Memory Usage: 31 MB, less than 5.25% of Python3 online submissions for Unique Paths II.
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        >>> s = Solution()
        >>> s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
        2
        >>> s.uniquePathsWithObstacles([[0,1],[0,0]])
        1
        >>> s.uniquePathsWithObstacles([[1,0]])
        0
        >>> s.uniquePathsWithObstacles([[1],[0]])
        0
        """
        rowNum, colNum = len(obstacleGrid), len(obstacleGrid[0])
        if (obstacleGrid[-1][-1] == 1): return 0
        if (rowNum == colNum and rowNum == 1): return 1
        sol = np.array([[0] * colNum for _ in range(rowNum)])

        sol[0] = 1
        sol[:, 0] = 1

        for rowIdx, row in enumerate(obstacleGrid):
            for colIdx, col in enumerate(row):
                if col == 1:
                    if colIdx == 0:
                        # sol[rowIdx:][colIdx] = -1     # TODO 这样写就是不行...索引...
                        sol[rowIdx:, colIdx] = -1
                    if rowIdx == 0:
                        sol[rowIdx, colIdx:] = -1

                    sol[rowIdx][colIdx] = -1

        # print(f"sol is {sol}")

        for row in range(1, rowNum):
            for col in range(1, colNum):
                if (sol[row][col] == -1): continue
                sol[row][col] += sol[row][col - 1] if sol[row][col - 1] != -1 else 0
                sol[row][col] += sol[row - 1][col] if sol[row - 1][col] != -1 else 0

        return sol[-1][-1] if sol[-1][-1] != -1 else 0
>>>>>>> hesy/master
