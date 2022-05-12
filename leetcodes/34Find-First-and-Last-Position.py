# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

from bisect import *


class Solution:
    def searchRange(self, nums, target):
        """
        >>> s = Solution()
        >>> s.searchRange([5,7,7,8,8,10],8)
        [3, 4]
        >>> s.searchRange([5,7,7,8,8,10],6)
        [-1, -1]
        >>> s.searchRange([],0)
        [-1, -1]
        """
        if not len(nums):
            return [-1, -1]
        lpos = bisect_left(nums, target)
        rpos = bisect_right(nums, target)
        # not exist:
        return [-1, -1] if lpos==len(nums) or nums[lpos] != target else [lpos, rpos-1]
