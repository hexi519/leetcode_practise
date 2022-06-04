# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def jump(self, nums):
        from sys import maxsize as MAX_INT
        minSteps = [MAX_INT for _ in range(len(nums))]
        minSteps[0] = 0
        for idx in range(len(nums) - 1):
            if len(nums) <= idx + nums[idx] + 1:
                minSteps[len(nums) - 1] = min(minSteps[len(nums) - 1], minSteps[idx] + 1)
                # print(f"\tquit idx is {idx},idx + nums[idx] + 1 is {idx + nums[idx] + 1} ")
                break

            for idxTo in range(idx + 1, idx + nums[idx] + 1):
                minSteps[idxTo] = min(minSteps[idxTo], minSteps[idx] + 1)

        # print(f"minSteps is {minSteps}")
        return minSteps[-1]


if __name__ == "__main__":
    sol = Solution()
    # print(f"res is {sol.jump([2, 3, 1, 1, 4])}")  # 2
    # print(f"res is {sol.jump([2,3,0,1,4])}")  # 2
    # print(f"res is {sol.jump([1])}")  # 0
    print(f"res is {sol.jump([1,2,3])}")  # 2
