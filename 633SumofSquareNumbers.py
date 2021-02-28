# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *

from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        >>> s = Solution()
        >>> s.judgeSquareSum(5)
        True
        >>> s.judgeSquareSum(3)
        False
        >>> s.judgeSquareSum(4)
        True
        >>> s.judgeSquareSum(2)
        True
        >>> s.judgeSquareSum(2)
        True
        """

        mid = int(sqrt(c / 2))
        right = int(sqrt(c))
        left = 0
        while left <= mid:
            if left**2 + right**2 > c:
                right = right - 1
            elif left**2 + right**2 == c:
                return True

            else:left = left + 1
        
        return False

