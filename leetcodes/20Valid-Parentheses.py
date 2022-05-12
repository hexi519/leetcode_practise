# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [easy]
'''

# TODO 试试看不用栈的方式

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


class Solution:
    def isValid(self, s: str) -> bool:
        """
        >>> sol = Solution()
        >>> sol.isValid("()[]{}")
        True
        >>> sol.isValid("([)]")
        False
        """
        st = []
        for letter in s:
            if letter in "([{" :
                st.append(letter)
            else:
                if letter == ")" and (not len(st) or st[-1]!='('):
                    return False
                elif letter == "]" and (not len(st) or st[-1]!='['):
                    return False
                elif letter == "}" and (not len(st) or st[-1]!='{'):
                    return False
                st.pop()
        if len(st):return False
        return True
