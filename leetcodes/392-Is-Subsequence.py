# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        >>> sol = Solution()
        >>> sol.isSubsequence("abc","ahbgdc")
        True
        >>> sol.isSubsequence("axc","ahbgdc")
        False
        >>> sol.isSubsequence("","")
        True
        >>> sol.isSubsequence("b","c")
        False
        """
        idx2, idx1 = -1, 0
        leng1, leng2 = len(s), len(t)
        if not leng1:
            return True
        if leng2 < leng1:
            return False

        # for alpha in s:
        while idx1 < leng1:
            if idx2 == leng2 - 1:
                return False

            while idx2 < leng2 - 1:
                idx2 += 1
                if s[idx1] == t[idx2]:
                    break
            idx1 += 1

        if idx2 < leng2 - 1 or (idx2 == leng2 - 1 and s[-1] == t[-1]):
            return True

        return False
