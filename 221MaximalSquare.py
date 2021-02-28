<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *


class Solution:
    # 再压缩一维...
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        >>> s = Solution()
        >>> s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
        4
        >>> s.maximalSquare([["0","1"],["1","0"]])
        1
        >>> s.maximalSquare([["0"]])
        0
        >>> s.maximalSquare([["1","1","1","1","1"],["1","1","1","1","1"],["0","0","0","0","0"],["1","1","1","1","1"],["1","1","1","1","1"]])
        4
        """
        rowNum, colNum = len(matrix), len(matrix[0])
        import numpy as np
        curLine = [0] * colNum
        # squareLen = [[0] * colNum for _ in range(rowNum)]  # 边长最大不过300
        maxLen = 0
        next_prev, prev = 0, 0
        for row in range(rowNum):
            # print(f"lineIdx {row}: curLine is ")
            for col in range(colNum):
                next_prev = curLine[col]

                # 这样的初始化有点愚蠢....最好的方法是最左边和最上边补一行0
                if matrix[row][col] == "0":
                    curLine[col] = 0
                    prev = next_prev
                    continue

                if (col == 0 or row == 0):
                    curLine[col] = 1
                    maxLen = max(maxLen, 1)
                else:
                    curLine[col] = 1 + min(curLine[col], curLine[col - 1], prev)
                    maxLen = max(maxLen, curLine[col])
                prev = next_prev

                # print(f"\tcurLine is {curLine}")

            # lastLine = curLine.copy()
            # curLine = [0] * colNum
        return maxLen * maxLen

    """
    # 两行一维数组优化空间
    # 优化了以后反而还没有之前的好...
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rowNum, colNum = len(matrix), len(matrix[0])
        import numpy as np
        curLine = [0] * colNum 
        # squareLen = [[0] * colNum for _ in range(rowNum)]  # 边长最大不过300
        maxLen = 0
        for row in range(rowNum):
            for col in range(colNum):
                if matrix[row][col] == "0" : continue
                if (col == 0 or row == 0) :
                    curLine[col] = 1
                    maxLen = max(maxLen, 1)
                else:
                    curLine[col] = 1 + min(lastLine[col],curLine[col-1],lastLine[col - 1])
                    maxLen = max(maxLen, curLine[col])
            lastLine = curLine.copy()
            curLine = [0] * colNum 
        return maxLen*maxLen
    """
    """"空间优化前
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rowNum, colNum = len(matrix), len(matrix[0])
        squareLen = [[0] * colNum for _ in range(rowNum)]  # 边长最大不过300
        maxLen = 0
        for row in range(rowNum):
            for col in range(colNum):
                if matrix[row][col] == "0" : continue
                if (col == 0 or row == 0) :
                    squareLen[row][col] = 1
                    maxLen = max(maxLen, 1)
                else:
                    
                    squareLen[row][col] = 1 + min(squareLen[row - 1][col],
                                                  squareLen[row][col - 1],
                                                  squareLen[row - 1][col - 1])
                    maxLen = max(maxLen, squareLen[row][col])

        return maxLen*maxLen
    """
=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *


class Solution:
    # 再压缩一维...
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        >>> s = Solution()
        >>> s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
        4
        >>> s.maximalSquare([["0","1"],["1","0"]])
        1
        >>> s.maximalSquare([["0"]])
        0
        >>> s.maximalSquare([["1","1","1","1","1"],["1","1","1","1","1"],["0","0","0","0","0"],["1","1","1","1","1"],["1","1","1","1","1"]])
        4
        """
        rowNum, colNum = len(matrix), len(matrix[0])
        import numpy as np
        curLine = [0] * colNum
        # squareLen = [[0] * colNum for _ in range(rowNum)]  # 边长最大不过300
        maxLen = 0
        next_prev, prev = 0, 0
        for row in range(rowNum):
            # print(f"lineIdx {row}: curLine is ")
            for col in range(colNum):
                next_prev = curLine[col]

                # 这样的初始化有点愚蠢....最好的方法是最左边和最上边补一行0
                if matrix[row][col] == "0":
                    curLine[col] = 0
                    prev = next_prev
                    continue

                if (col == 0 or row == 0):
                    curLine[col] = 1
                    maxLen = max(maxLen, 1)
                else:
                    curLine[col] = 1 + min(curLine[col], curLine[col - 1], prev)
                    maxLen = max(maxLen, curLine[col])
                prev = next_prev

                # print(f"\tcurLine is {curLine}")

            # lastLine = curLine.copy()
            # curLine = [0] * colNum
        return maxLen * maxLen

    """
    # 两行一维数组优化空间
    # 优化了以后反而还没有之前的好...
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rowNum, colNum = len(matrix), len(matrix[0])
        import numpy as np
        curLine = [0] * colNum 
        # squareLen = [[0] * colNum for _ in range(rowNum)]  # 边长最大不过300
        maxLen = 0
        for row in range(rowNum):
            for col in range(colNum):
                if matrix[row][col] == "0" : continue
                if (col == 0 or row == 0) :
                    curLine[col] = 1
                    maxLen = max(maxLen, 1)
                else:
                    curLine[col] = 1 + min(lastLine[col],curLine[col-1],lastLine[col - 1])
                    maxLen = max(maxLen, curLine[col])
            lastLine = curLine.copy()
            curLine = [0] * colNum 
        return maxLen*maxLen
    """
    """"空间优化前
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rowNum, colNum = len(matrix), len(matrix[0])
        squareLen = [[0] * colNum for _ in range(rowNum)]  # 边长最大不过300
        maxLen = 0
        for row in range(rowNum):
            for col in range(colNum):
                if matrix[row][col] == "0" : continue
                if (col == 0 or row == 0) :
                    squareLen[row][col] = 1
                    maxLen = max(maxLen, 1)
                else:
                    
                    squareLen[row][col] = 1 + min(squareLen[row - 1][col],
                                                  squareLen[row][col - 1],
                                                  squareLen[row - 1][col - 1])
                    maxLen = max(maxLen, squareLen[row][col])

        return maxLen*maxLen
    """
>>>>>>> hesy/master
