# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *


import collections
class Solution(object):
    def findMaxForm(self,S,m,n):
        S = [collections.Counter(s) for s in S]
        S = [[s['0'],s['1']] for s in S]
        dp = [ [0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, len(S)+1):
            zero, one = S[i-1]
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    if j>=zero and k>=one:
                        dp[j][k] = max(dp[j][k], dp[j-zero][k-one]+1)
                    else:
                        dp[j][k] = dp[j][k]
        return dp[m][n]