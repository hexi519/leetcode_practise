# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution(object):
    def numDecodings(self, s):
        """
        >>> s = Solution()
        >>> s.numDecodings("12")
        2
        >>> s.numDecodings("226")
        3
        >>> s.numDecodings("106")
        1
        >>> s.numDecodings("06")
        0
        """
        if s[0] == '0':
            return 0
        from collections import defaultdict
        pre_, pre, ans = 1, 1, 1  # dp[0],dp[-1]
        for i in range(1, len(s)):
            flag = 0 < int(s[i-1:i+1]) < 27 and s[i-1] != '0'
            if s[i] == '0':
                if flag:
                    ans = pre_
                else:
                    return 0
            else:
                ans += pre_ if flag else 0
            pre_, pre = pre, ans
            # log.info( f"cur is {s[i]},updated pre_, pre, ans is {pre_},{pre},{ans}")
        return ans
