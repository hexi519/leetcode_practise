# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy]
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        >>> s = Solution()
        >>> s.twoSum([2,7,11,15],9)
        [0, 1]
        >>> s.twoSum([3,2,4],6)
        [1, 2]
        >>> s.twoSum([3,3],6)
        [0, 1]
        """
        begin, end = 0, len(nums)-1
        import numpy as np
        idx,nums_ = np.argsort(nums),sorted(nums)    
        while begin < end:
            if nums_[begin]+nums_[end] > target:
                end -= 1
            elif nums_[begin]+nums_[end] < target:
                begin += 1
            else:
                return [idx[begin], idx[end]]
        """
        from collections import defaultdict
        hashTable = defaultdict(lambda: -1)
        for idx, number in enumerate(nums):
            query = target - number
            if hashTable[query] != -1:    # 存在
                return [hashTable[query], idx]
            else:   # 不存在对应的，存入
                hashTable[number] = idx
        """
