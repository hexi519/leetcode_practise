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

from collections import defaultdict


class Solution:
    def helper(self, nums, idx, target, dp):
        if idx == len(nums):
            return 1 if target == 0 else 0

        curStr = str(idx) + ',' + str(target)

        # print(f"curStr is {curStr}")
        # print(f"dp is {dp}")

        if curStr in dp.keys():
            return dp[curStr]

        ans = 0
        ans += self.helper(nums, idx + 1, target - nums[idx], dp)
        ans += self.helper(nums, idx + 1, target + nums[idx], dp)
        dp[curStr] = ans
        return ans

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """#回溯的思路"""
        if sum(nums) < abs(target):
            return 0
        dp = defaultdict(int)
        return self.helper(nums, 0, target, dp)
        """ #*划分等价子集的思路
        value = (sum(nums) + target) // 2
        if value < (sum(nums) + target) / 2 or sum(nums) < abs(target):
            return 0

        # dp表示能装的方法的数量
        dp = [[0 for _ in range(value + 1)] for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for val in range(value + 1):
            for idx in range(1, len(nums) + 1):
                wei = nums[idx - 1]
                dp[idx][val] = dp[idx - 1][val]  # not chooses
                if val >= wei:
                    dp[idx][val] += dp[idx - 1][val - wei]  #+ dp[idx][val]  # choose

        return dp[-1][-1]
        """


if __name__ == '__main__':
    sol = Solution()
    nums, target = [1, 1, 1, 1, 1], 3
    nums, target = [100], -200
    # nums, target = [1], 1
    nums, target = [1, 0], 1
    print(f"res is {sol.findTargetSumWays(nums, target)}")
"""
# 自底向上的memo写法
class Solution(object):
    def findTargetSumWays(self, nums, S):
        from collections import defaultdict
        memo = {0: 1}
        for x in nums:
            m = defaultdict(int)
            for s, n in memo.items():
                m[s + x] += n
                m[s - x] += n
            memo = m
        return memo[S]
"""