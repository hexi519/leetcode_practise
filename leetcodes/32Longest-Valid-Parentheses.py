# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


# dp和栈
class Solution:
    def longestValidParentheses(self, chars: str) -> int:
        """
        >>> sol = Solution()
        >>> sol.longestValidParentheses("(()")
        2
        >>> sol.longestValidParentheses(")()())")
        4
        >>> sol.longestValidParentheses("")
        0
        >>> sol.longestValidParentheses("()(()")
        2
        >>> sol.longestValidParentheses("()(())")
        6
        >>> sol.longestValidParentheses(")(")
        0
        >>> sol.longestValidParentheses("(()))())(")
        4
        """
        # dp method
        dp = [0] * len(chars)  
        if not dp: return 0
        for index in range(len(chars)):
            if chars[index] == '(' or index == 0:
                continue
            else:
                if chars[index - 1] == '(':  # ...()
                    dp[index] = dp[index - 2] + 2
                else:  #...))
                    if index - dp[index - 1] - 1 >= 0 and chars[index - dp[index - 1] - 1] == '(':
                        dp[index] = dp[index - 1] + 2 + dp[index - dp[index - 1] - 2]

        return max(dp)

        #* stack method
        indexStack = [-1]
        ans = 0
        for index in range(len(chars)):
            if chars[index] == '(':
                indexStack.append(index)
            if chars[index] == ')':
                if indexStack[-1] == -1 or chars[indexStack[-1]] != '(':
                    indexStack.append(index)
                else:  # chars[indexStack[-1] ]=='(':
                    indexStack.pop()
                    ans = max(ans, index - indexStack[-1])

        return ans
