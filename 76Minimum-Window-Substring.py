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
    def minWindow(self, forQuery, query):
        """
        >>> sol = Solution()
        >>> sol.minWindow("ADOBECODEBANC","ABC")
        'BANC'
        >>> sol.minWindow("a","a")
        'a'
        >>> sol.minWindow("aa","aa")
        'aa'
        """
        need = len(query)
        from collections import defaultdict
        queryNeed, queryFind = defaultdict(int), defaultdict(int)  # 需要找的，已经找到的
        toQuerySet = set(query)
        for ch in query:
            queryNeed[ch] += 1
        slow, fast = 0, 0
        ans = [0, len(forQuery)]

        while fast < len(forQuery):
            if forQuery[fast] in toQuerySet:
                queryFind[forQuery[fast]] += 1
                if queryFind[forQuery[fast]] <= queryNeed[forQuery[fast]]:  # the first time for meeting
                    need -= 1
            fast += 1

            while slow < fast:  # 没毛病 因为len至少为1，所以重叠的情况可以不考虑(初始化的时候也是)
                if forQuery[slow] in toQuerySet:
                    if queryFind[forQuery[slow]] <= queryNeed[forQuery[slow]]:
                        break   # 不能再右移了
                    else:
                        queryFind[forQuery[slow]] -= 1
                slow += 1

            if (not need) and (fast - slow < ans[1] - ans[0]):
                ans = [slow, fast]

        if (not need) and (fast - slow < ans[1] - ans[0]):
            ans = [slow, fast]

        if need:
            return ""

        else:
            return forQuery[ans[0]:ans[1]]
