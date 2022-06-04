# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] dp
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2: return True
        interv = dict()
        for idx in range(len(nums)):
            interv[idx] = idx + nums[idx]

        sorted_interv = sorted(interv.keys())  # list of start pos,representing each interval
        # print(f"interv is {interv}")

        merged = [False for _ in range(len(sorted_interv))]
        merged[0] = True
        endPos = interv[sorted_interv[0]]

        count = 0
        while count < len(interv):
            # print(f"endPos is {endPos}, and merged is {merged}")
            for idx in range(1, len(sorted_interv) - 1):
                if not merged[idx]:
                    newStartPos = sorted_interv[idx]
                    # print(f"\tnewStartPos is {newStartPos}")
                    if endPos >= newStartPos:  # end > start
                        endPos = max(endPos, interv[newStartPos])
                        merged[idx] = True
                    else:
                        break

            if endPos >= len(nums) - 1:
                return True

            count += 1

        return False


if __name__ == '__main__':
    sol = Solution()
    print(f"res is {sol.canJump([2, 3, 1, 1, 4])}")
    print(f"res is {sol.canJump([1,1,0])}")
    print(f"res is {sol.canJump([1])}")
    print(f"res is {sol.canJump([1,0,1])}")
    print(f"res is {sol.canJump([3, 2, 1, 0, 4])}")