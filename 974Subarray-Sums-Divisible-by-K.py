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
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        """
        >>> s = Solution()
        >>> s.subarraysDivByK([4,5,0,-2,-3,1],5)
        7
        >>> s.subarraysDivByK([4,5,0,-2,-3,1,0],5)
        9
        >>> s.subarraysDivByK([],5)
        0
        >>> s.subarraysDivByK([5],9)
        0
        """
        count = 0
        from collections import defaultdict
        record = defaultdict(int)
        preSum = 0
        # 边计算前缀和 便处理 复杂度: O(n)
        for number in A:
            preSum += number
            afterDi = preSum % K
            count += record[afterDi]
            record[afterDi] += 1
            if not afterDi: # 本身余数是0的话，也得加上
                count += 1
        return count
