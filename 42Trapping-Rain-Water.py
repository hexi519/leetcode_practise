# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard] 接雨水
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


# TODO 动规和单调栈都做一遍
class Solution:
    def trap(self, heights: List[int]) -> int:
        """
        >>> sol = Solution()
        >>> sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
        6
        """
        allNum = len(heights)
        maxl, maxr = [0] * allNum, [allNum - 1] * allNum
        for index in range(allNum):
            if index == 0:
                continue
            maxl[index] = maxl[index - 1] if heights[maxl[index - 1]] > heights[index - 1] else index - 1

        # for index, height in enumerate(heights)[::-1]:
        for index in range(allNum)[::-1]:
            if index == allNum - 1:
                continue
            maxr[index] = maxr[index + 1] if heights[maxr[index + 1]] > heights[index + 1] else index + 1

        log.info(f"maxl is {maxl}")
        log.info(f"maxr is {maxr}")

        curIndex, ans = 0, 0
        while curIndex < allNum:
            li, ri = maxl[curIndex], maxr[curIndex]
            minHeight = min(heights[li], heights[ri])
            log.info(f'li,ri of curIndex {curIndex}({heights[curIndex]}) is {li}({heights[li]}),{ri}({heights[ri]})')
            log.info(f"\tminHeight,ans is {minHeight},{ans}")
            while curIndex < ri:
                if curIndex == li:
                    curIndex += 1
                    continue
                ans += minHeight - heights[curIndex]
                curIndex += 1
            curIndex += 1  # jump over rightHeight
        return ans
        """ # monoStack
        # TODO 还得想下corner case
        monoStack = []
        allNum = len(heights)
        left, right = [0] * allNum, [allNum - 1] * allNum  # TODO check
        for index, height in enumerate(heights):
            # log.info(f"cur height is {index}({height}), monoStack is {monoStack}")
            if index == 0:
                monoStack.append(index)
                continue
            while len(monoStack) and height > heights[monoStack[-1]]:
                # TODO 这里没写对，因为实在没想好，左右单调栈咋处理
                popIndex = monoStack.pop()
                right[popIndex] = index if not right[popIndex]==allNum - 1 else right[popIndex]
            if  len(monoStack):
                left[index] = monoStack[-1]  # TODO 考虑到最高个没有左边的
                if heights[monoStack[-1]] == height:
                    right[monoStack[-1]]=index
            monoStack.append(index)

        curIndex, ans = 0, 0
        while curIndex < allNum:
            li, ri = left[curIndex], right[curIndex]
            minHeight = min(heights[li], heights[ri])
            log.info(f'li,ri of curIndex {curIndex}({heights[curIndex]}) is {li}({heights[li]}),{ri}({heights[ri]})')
            log.info(f"\tminHeight,ans is {minHeight},{ans}")
            while curIndex < ri:
                if curIndex==li : 
                    curIndex+=1
                    continue
                ans += minHeight - heights[curIndex]
                curIndex += 1
            curIndex += 1   # jump over rightHeight
        return ans
        """
