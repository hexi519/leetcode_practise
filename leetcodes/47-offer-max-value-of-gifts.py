# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]   剑指offer
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        """
        >>> s = Solution()
        >>> s.maxValue([[1,3,1],[1,5,1],[4,2,1]])
        12
        >>> s.maxValue([[1]])
        1
        """
        # corner case
        rowNum, colNum = len(grid), len(grid[0])
        if rowNum==1 and colNum==0: return 0
        # log.info(f"dp is {type(dp)}, and {dp}")
        for row in range(rowNum):
            for col in range(colNum):
                gift = max(grid[row][col-1] if col-1 >=0 else 0, 0)
                gift = max(grid[row-1][col] if row-1 >=0 else 0, gift)
                grid[row][col] += gift
                # log.info(f"grid is {grid}")

        return grid[rowNum-1][colNum-1]
