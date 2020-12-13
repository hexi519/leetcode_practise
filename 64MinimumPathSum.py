# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *

### 其实根本不需要另开一个数组啊...就直接更新grid数组就可以了哇...
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        >>> s = Solution()
        >>> s.minPathSum([[1]])
        1
        >>> s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
        7
        >>> s.minPathSum([[1,2,3],[4,5,6]])
        12
        """
        rowNum = len(grid) 
        colNum = len(grid[0]) 
        dist = [401] * colNum 

        dist[0] = grid[0][0]
        for i in range(1, colNum):
            dist[i]=dist[i-1]+grid[0][i]

        for rowIdx in range(1, rowNum):
            # for colIdx in range(colNum-1,-1,-1):
            dist[0]=dist[0]+grid[rowIdx][0]
            for colIdx in range(1,colNum):
                dist[colIdx]= min(dist[colIdx-1],dist[colIdx])+grid[rowIdx][colIdx]
        
        return dist[-1]
    