# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from tkinter import SOLID
from typing import Dict, List
from util import *
# from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        srcX,srcY = startPos[0],startPos[1]
        dstX,dstY = homePos[0],homePos[1]
        res = 0
        if dstX<srcX:
            for idx in range(srcX-1,dstX-1,-1):
                res+=rowCosts[idx]
        else: 
            for idx in range(srcX+1,dstX+1):
                res+=rowCosts[idx]
        
        if dstY<srcY:
            for idx in range(srcY-1,dstY-1,-1):
                res+=colCosts[idx]
        else: 
            for idx in range(srcY+1,dstY+1,):
                res+=colCosts[idx]

        return res
    
    def minCost_dp(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        lenR,lenC = len(rowCosts),len(colCosts)
        srcX,srcY = startPos[0],startPos[1]
        dstX,dstY = homePos[0],homePos[1]
        # move to a same side
        if srcY>dstY:
            # left - right inverse
            for col in range(lenC):
                col = col[::-1]

            # change index-1
            srcY = lenR-1-srcY
            dstY = lenR-1-dstY
    
        if srcX>dstX:
            # up - down inverse
            for row in range(lenR):
                row = row[::-1]

            # change index-0
            srcX = lenC-1-srcX
            srcY = lenC-1-srcY
        
        dp = [[0 for _ in range(lenC)] for _ in range(lenR)]

        for idxR in range(srcX+1,lenR):
            dp[idxR][0] += rowCosts[idxR]
        
        for idxC in range(srcY+1,lenC):
            dp[0][idxC] += colCosts[idxC]

        for idxR in range(srcX+1,dstX+1):
            for idxC in range(srcY+1,dstY+1):
                dp[idxR][idxC] = min(dp[idxR-1][idxC]+rowCosts[idxR],dp[idxR][idxC-1]+colCosts[idxC])
                print(f"dp is {dp}")

        return dp[dstX][dstY]

if __name__ == "__main__":
    sol = Solution()
    startPos,homePos= [1,0],[2, 3]
    rowCosts ,colCosts =[5,4,3],[8,2, 6, 7]
    print(f"res is {sol.minCost(startPos, homePos, rowCosts, colCosts)}")