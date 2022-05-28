# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        >>> s = Solution()
        >>> s.isMatch("aab","c*a*b")
        True
        >>> s.isMatch("aa","a*")
        True
        >>> s.isMatch("aa","a")
        False
        >>> s.isMatch("aa","a*")
        True
        >>> s.isMatch("mississippi","mis*is*p*.")
        False
        """
        lenObj, lenPattern = len(s), len(p)
        dp = [[False for _ in range(lenPattern+1)] for __ in range(lenObj+1)]
        dp[0][0] = True
        
        def match(i ,j):    # 不包括*在内的match
            if i ==0 :
                return False
            if s[i-1]==p[j-1] or p[j-1] ==".":
                return True
            return False

        for i in range(lenObj+1):
            for j in range(1,lenPattern+1):
                if p[j-1] =="*":    
                    if match(i,j-1):  
                        # x* match 0次 
                        dp[i][j] |= dp[i][j-2]
                        # x* Match 1次 ， index到j-3的 和 index到i-1的去match
                        dp[i][j] |= dp[i][j-1]
                        # x* Match n次 ， 之前x*已经有match过的了, 所以只要 到index为i-2的 和 到index为j-1(including了x*)的能匹配得上，就行 --》 不用管 到index为i-2的 到底有没有存在匹配，反正是个或，有最好，没有的话顶多 或了个 False，不会有影响 #* 这个比较难理解，可能需要背一下
                        dp[i][j] |= dp[i-1][j]

                    else:   # \ *前面的和人家也不match的话，相当于 index到j-2的 和 index到i-1的去match
                        dp[i][j] |= dp[i][j-2]

                else:
                    if match(i,j):
                        dp[i][j] |= dp[i-1][j-1]
        
        return dp[-1][-1]
