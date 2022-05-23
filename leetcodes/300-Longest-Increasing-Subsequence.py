# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] dp
'''

from typing import Dict, List
from util import *
# from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.lengthOfLIS([10,9,2,5,3,7,101,18])
        4
        >>> s.lengthOfLIS([0,1,0,3,2,3])
        4
        >>> s.lengthOfLIS([7,7,7,7,7,7,7])
        1
        """
        dp = [1 for _ in  range(len(nums))]
        res = 1
        for idx in range(1,len(nums)):
            for j in range(idx):
                dp[idx] = max(dp[idx], (dp[j]+1) if nums[idx]>nums[j] else dp[idx])
            
            res = max(res,dp[idx])

        return res


if __name__ == "__main__":
    sol = Solution()
    print(f"res is {sol.lengthOfLIS([4,10,4,3,8,9])}")
    