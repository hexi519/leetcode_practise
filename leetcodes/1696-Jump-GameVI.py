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

from sys import maxsize as MAX_INT


class Solution:
    # from collections import defaultdict
    # memo = dict()

    def dp(self, nums, idx, k):
        # print(f"idx is {idx}, self.memo is {self.memo}")
        if self.memo.get(idx, 1 - MAX_INT) != 1 - MAX_INT:
            return self.memo[idx]

        curVal = 1 - MAX_INT
        # for idx in range(len(nums) - 1):
        for nextIdx in range(idx + 1, min(idx + k + 1, len(nums))):
            curVal = max(self.dp(nums, nextIdx, k), curVal)

        self.memo[idx] = curVal + nums[idx]

        return self.memo[idx]

    def maxResult(self, nums: List[int], k: int) -> int:
        # self.memo.default_factory = 1 - MAX_INT  # TODO how to use
        self.memo = dict()
        self.memo[len(nums) - 1] = nums[len(nums) - 1]
        return self.dp(nums, 0, k)

    def greedyMaxResult(self, nums: List[int], k: int) -> int:
        curIdx = 0
        res = 0
        while curIdx < len(nums):
            # print(f"curIdx,last res is {curIdx},{res}")
            res += nums[curIdx]
            nextIdx = curIdx + 1
            maxNextIdx = nextIdx
            while nextIdx < min(len(nums), curIdx + k + 1):
                if nums[nextIdx] > 0:
                    curIdx = nextIdx
                    break

                if nums[maxNextIdx] < nums[nextIdx]:
                    maxNextIdx = nextIdx

                nextIdx += 1

            if nextIdx < min(len(nums), curIdx + k + 1):  # ugly writing
                # print(f"\tcontinue with nextIdx of {nextIdx},maxNextIdx of {maxNextIdx}")
                continue

            curIdx = maxNextIdx

        return res


if __name__ == "__main__":
    sol = Solution()
    nums, k = [1, 2, 3, 4], 2  # 10
    nums, k = [1, -1, -2, 4, -7, 3], 2  # 7
    # nums, k = [1, -5, -20, 4, -1, 3, -6, -3], 2  # 0
    # nums, k = [-5], 2  # -5
    nums, k = [1, -1, -2, -3, 0], 2  # -1
    # nums, k = [1, -3, -2, -1, 0], 2  # -1

    nums, k = [10, -5, -2, 4, 0, 3], 3  # 17
    print(f"res is {sol.maxResult(nums,k)}")
