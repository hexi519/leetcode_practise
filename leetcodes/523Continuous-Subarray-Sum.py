# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log
class Solution:
    def checkSubarraySum(self, nums: List[int], K: int) -> bool:
        """
        >>> s = Solution()
        >>> s.checkSubarraySum([23,2,4,6,7],6)
        True
        >>> s.checkSubarraySum([23,2,6,4,7],6)
        True
        >>> s.checkSubarraySum([],5)
        False
        >>> s.checkSubarraySum([0],1)
        False
        >>> s.checkSubarraySum([1,0],2)
        False
        >>> s.checkSubarraySum([23,2,6,4,7],13)
        False
        """
        count = 0
        from collections import defaultdict
        record = defaultdict(int)
        preSum = 0
        # 边计算前缀和 便处理 复杂度: O(n)
        for number in nums:
            preSum += number
            afterDi = preSum % K
            count += record[(K-afterDi)%K]
            record[afterDi] += 1
            # if not afterDi and preSum: # 本身余数是0的话，也得加上
            #     count += 1
            
            if count:
                return True

        return False
