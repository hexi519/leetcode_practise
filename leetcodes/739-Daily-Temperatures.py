# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] monotone stack
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        >>> sol = Solution()
        >>> sol.dailyTemperatures([73,74,75,71,69,72,76,73])
        [1, 1, 4, 2, 1, 1, 0, 0]
        >>> sol.dailyTemperatures([30,40,50,60])
        [1, 1, 1, 0]
        >>> sol.dailyTemperatures([30,60,90])
        [1, 1, 0]
        >>> sol.dailyTemperatures([89,62,70,58,47,47,46,76,100,70])
        [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
        """
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for index in range(len(temperatures)):
            while len(stack) and temperatures[stack[-1]] < temperatures[index]:
                popIdx = stack.pop()
                res[popIdx] = index - popIdx

            stack.append(index)
            # print(f"temp[{index}]({temperatures[index]}) with stack of {stack}")

        return res


if __name__ == "__main__":
    sol = Solution()
    arrs = [73, 74, 75, 71, 69, 72, 76, 73]
    # arrs = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    # arrs = [30, 60, 90]
    print(f"res is {sol.dailyTemperatures(arrs)}")
