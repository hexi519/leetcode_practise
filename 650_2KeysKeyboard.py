# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] 650_2KeysKeyboard  
'''

from typing import Dict, List
from util import *
class Solution:
    def minSteps(self, n: int) -> int:

        dp = [n]*(n+1)
        dp[1]=0     # 这里要注意，最终值是1，会在循环里面更新
        from math import sqrt
        for i in range(1,n+1):
            """
            原本的版本是遍历所有的j(from 1 to i)取最小的dp(j)+1，现在是找到第一个最大的因子就计算Eq.(1)返回，速度一下子快了很多（from "beats 40%" to "beats 60%"(methos2) ）
            >>> Eq.(1)为何是最优的：想想也知道....能copy大段肯定比小段小段copy要好啊...
            >>> 一定要找最大公因式。或者是整除最大公因式的因式也可以。具体的可以举例想想( dp[18]=dp[9]+2 != dp[3]+6 )
            一种方法是找最小因子x，然后通过n/x获得最大因子，然后利用Eq.(1)计算。但是这种方法要 j from 2 to sqrt(n)，且找不到最小公因子的情况(质数)要另外考虑，代码比较繁，但是搜的会更少。
            另一种方法是直接找最大公因子。由于找的是最大的因子，所以不能从sqrt(n)递减遍历了，得从i开始递减。但是由于i-j>=j，所以可以优化到从i/2开始递减。（这里又有两种实现方法，如下）
            """
            # method1
            for j in range(int(i/2),int(sqrt(i))-1,-1):   # 这里的上下界想清楚    # int是fix()取整
                if not i%j:
                    dp[i]=dp[j]+int(i/j)
                    break
            if(dp[i]==n):
                dp[i]=i
            # method2
            """
            for j in range(int(i/2),1,-1):      # 顺带连边界情况都考虑进来了
                if not i%j:
                    dp[i]=dp[j]+int(i/j)
                    break
            """
        return dp[n]
"""
if __name__ == "__main__":
    print("here is main")
    s = Solution()
    print(f"res is {s.minSteps(18)}")
    print(f"res is {s.minSteps(12)}")
"""

class Solution:
    def minSteps(self, n: int) -> int:
        """
        >>> s = Solution()
        >>> s.minSteps(3)
        3
        >>> s.minSteps(1)
        0
        >>> s.minSteps(18)
        8
        >>> s.minSteps(12)
        7
        >>> s.minSteps(7)
        7
        """
        # return 0 if n==1
        from collections import defaultdict
        # dp, helper = [2000] * (n + 1), [set() for _ in range(n + 1)]
        # dp[1] = 0
        # helper[1].add(0)
        dp = [defaultdict(lambda: 2000) for _ in range(n + 1)]
        dp[1][0] = 0
        for curNum in range(n + 1):
            for pasteNum in dp[curNum].keys():
                if curNum + pasteNum < n + 1:
                    dp[curNum + pasteNum][pasteNum] = min(dp[curNum][pasteNum] + 1,
                                                          dp[curNum + pasteNum][pasteNum])
                    # helper[curNum + pasteNum].add(pasteNum)
            if curNum * 2 < n + 1 and len(dp[curNum]):
                dp[curNum * 2][curNum] = min(min(dp[curNum].values()) + 2, dp[curNum * 2][curNum])
                # helper[curNum * 2].add(curNum)

            # print(f"curNum:{curNum}:\n\tdp is {dp}")
            # print(f"curNum:{curNum}:\n\tdp is {dp} \n\thelper is {helper}")

        return min(dp[-1].values())

# if __name__ == "__main__":
#     s = Solution()
#     print(f"res is {s.minSteps(7)}")