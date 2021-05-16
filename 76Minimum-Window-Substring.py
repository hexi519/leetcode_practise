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

# TODO 特殊case，重新读下题，看看 "aa","aa" --> "aa" 这种情况题目覆盖了没有
# TODO 看下follow-up...难道正常不就应该是我这么做么....

class Solution:
    def minWindow(self, s, t):
        """
        >>> sol = Solution()
        >>> sol.minWindow("ADOBECODEBANC","ABC")
        'BANC'
        >>> sol.minWindow("a","a")
        'a'
        """
        need = len(t)
        from collections import defaultdict
        toFind = set(t)
        find = defaultdict(int)  # 有必要记录数字么 --> 有2333
        slow, fast = 0, 0
        ans = [0, len(s)]

        while fast < len(s):

            if s[fast] in toFind:
                find[s[fast]] += 1
                if find[s[fast]] == 1:  # the first time for meeting
                    need -= 1
            fast += 1
            # log.info(f"fast forwards to {fast},and need is {need}")
            # log.info(f"find is {[(key,value)for key,value in find.items()]}")

            while slow < fast:  # 没毛病 因为len至少为1，所以重叠的情况可以不考虑(初始化的时候也是)
                if s[slow] in toFind:
                    if find[s[slow]] == 1:
                        break
                    else:
                        find[s[slow]] -= 1
                slow += 1

            # log.info(f"slow forwards to {slow},and need is {need}")

            if (not need) and (fast - slow < ans[1] - ans[0]):
                ans = [slow, fast]

        if (not need) and (fast - slow < ans[1] - ans[0]):
            ans = [slow, fast]
            # log.info(f"****record ans to be {ans}****")


        if need:
            return ""

        else:
            return s[ans[0]:ans[1]]