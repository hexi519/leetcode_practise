# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from collections import deque

# 数组元素不超过1e4, 至少有一个0，保证输入数据的有效性
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        >>> s = Solution()
        >>> s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        >>> s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
        [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        >>> s.updateMatrix([[0]])
        [[0]]
        >>> s.updateMatrix([[0],[0],[0],[0],[0]])
        [[0], [0], [0], [0], [0]]
        """
        rowNum,colNum = len(matrix), len(matrix[0])
        dist = [[20000] * colNum for _ in range(rowNum)]  # 边长最大不过10000 
        queue_helper = deque()
        for rowIdx in range(rowNum):
            for colIdx in range(colNum):
                if not matrix[rowIdx][colIdx]:
                    queue_helper.append((rowIdx, colIdx))
                    dist[rowIdx][colIdx] = 0

        while len(queue_helper):
            cur_rIdx, cur_cIdx = queue_helper.popleft()
            for rIdx, cIdx in [(cur_rIdx - 1, cur_cIdx),
                               (cur_rIdx, cur_cIdx - 1),
                               (cur_rIdx + 1, cur_cIdx),
                               (cur_rIdx, cur_cIdx + 1)]:
                if -1 < rIdx and rIdx < rowNum and -1 < cIdx and cIdx < colNum and dist[rIdx][cIdx]==20000:
                    dist[rIdx][cIdx] = dist[cur_rIdx][cur_cIdx] + 1
                    queue_helper.append( (rIdx, cIdx) )

        return dist

