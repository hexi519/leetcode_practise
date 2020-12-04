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
        """
        >>> s = Solution()
        >>> s.minSteps(18)
        8
        >>> s.minSteps(12)
        7
        """
        dp = [n]*(n+1)
        dp[1]=0     # 这里要注意，最终值是1，会在循环里面更新
        from math import sqrt
        for i in range(1,n+1):
            """
            原本的版本是遍历所有的j(from 1 to i)取最小的dp(j)+1，现在是找到第一个最大的因子就计算Eq.(1)返回，速度一下子快了很多（from "beats 40%" to "beats 60%"(methos2) ）
            >>> #TODO Eq.(1)为何是最优的，实际上是可以证明的(找找别人的证明) --》 看下中文版的leetcode官方解释(https://leetcode-cn.com/problems/2-keys-keyboard/solution/zhi-you-liang-ge-jian-de-jian-pan-by-leetcode/)
            >>> #TODO naive DP是怎么算过来的（阶段定义为n个阶段，为何还要个[j]的第二个维度(肯定是需要的，但具体为什么还没想清楚) ），以及为何可以状态压缩，还需要想想
            >>> #TODO 结合stage和state的思想，考虑下背包 和找零钱问题 怎么思考
            >>> #TODO 再看看这个大佬有没有讲解别的(https://leetcode-cn.com/problems/2-keys-keyboard/solution/dong-tai-gui-hua-xiang-xi-fen-xi-jie-shi-wei-shi-y/)
            >>> 一定要找最大公因式。或者是整除最大公因式的因式也可以。具体的可以举例想想( dp[18]=dp[9]+2 != dp[3]+6 )
            一种方法是找最小因子x，然后通过n/x获得最大因子，然后利用Eq.(1)计算。但是这种方法要 j from 2 to sqrt(n)，且找不到最小公因子的情况(质数)要另外考虑，代码比较繁，但是搜的会更少。
            另一种方法是直接找最大公因子。由于找的是最大的因子，所以不能从sqrt(n)递减遍历了，得从i开始递减。但是由于i-j>=j，所以可以优化到从i/2开始递减。
            """
            # method1
            """
            for j in range(int(i/2),int(sqrt(i))-1,-1):   # 这里的上下界想清楚    # int是fix()取整
                if not i%j:
                    dp[i]=dp[j]+int(i/j)
                    break
            if(dp[i]==n):
                dp[i]=i
            """
            # method2
            for j in range(int(i/2),1,-1):      # 顺带连边界情况都考虑进来了
                if not i%j:
                    dp[i]=dp[j]+int(i/j)
                    break
        return dp[n]


if __name__ == "__main":
    print("here is main")
    s = Solution()
    print(f"res is {s.minSteps(18)}")
    print(f"res is {s.minSteps(12)}")
