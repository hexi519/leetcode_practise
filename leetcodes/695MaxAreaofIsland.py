# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy]
'''

from typing import Dict, List
from util import *

class Solution:
    # method 1 : 遍历过后删除1
    def maxAreaOfIsland(self, grid):
        res = 0
        if not len(grid) or len(grid[0]) : return 0
        rowNum , colNum = len(grid) , len(grid[0])

        from collections import deque
        onesStack = deque   # bfs
        for rowIdx in range rowNum:
            for colIdx in range colNum:
                if()
            

    # method 2 : dp