# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard] [dp series]
'''

from typing import Dict, List
from util import *

import numpy as np

#* 最简单的能想到的就是 dp[stone][action]，其中stone和action都是 [1:max(stones)] , 因为我们在某个stone处，其实我们也不知道前面一步具体是多少。这个的问题是，直接out of memory。把dp矩阵打印出来也可以发现大部分都是False，which means是稀疏矩阵。也就是说我们的阶段和状态定义的不好。
# > 太可怕了，这个一开始的想法也太愚蠢了吧...

# 我们的阶段实际上就只有stones数组里面的几个数值，并不是连续值，所以阶段就是[stone in stones]。紧接着就是action的设计考量：
# 想法1：action实际上不会超过1100（每步只会增加1，一共最多输入1100个数，还包括0）。但这个想法就是有点浪费空间，因为还是很多action是取不到的。https://blog.csdn.net/da_kao_la/article/details/105176065。 但这里的更新方式就比较值得玩味了，是for i in range(len(stones)): for j in range(len(i)+1), 而不是常规的for i in range(len(stones)): for j in range(action_lens),所以就比较难想。但是如果按照常规的for循环更新，就会设计到查找的优化。下文会体现。
# 想法2：一个地方只能从前面的某个石子跳过来，which means也不是连续整数值可选，所以其实也只有O(num(stones))的可选项。所以又回到打家劫舍的问题的里面去了： 前i个stone，所以设计为dp[stone][stone]表示的就是从stone_idx2跳到stone_idx1是否可行。如下，但是每次状态转移，需要搜索stones的list( O(n) )，最后就是O(n^3)的复杂度了--> O(10^9)直接超时。

#* 改进思路： 降低查找的复杂度
# 常用方法1：二分搜索，O(n^3) --> O(n^2*logn)
# 常用方法2：使用额外的、低查找开销的数据结构存储经常要查找的东西。这里使用hashMap,所以每次就不是搜数组，而是搜一个集合。

# TODO 一秒是不是只可以处理10^8数量级来着

#* Version1 :orginal Out of Time Limit version
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        >>> s = Solution()
        >>> s.canCross([0,1,3,5,6,8,12,17])
        True
        >>> s.canCross([0,1,2,3,4,8,9,11])
        False
        """
        numStep = len(stones)
        # print(f"numStep is {numStep}")
        dp = np.array([[False] * numStep
                       for _ in range(numStep)])  # 目前是step的位置，上一步跳了action
        dp[0, 0] = True
        # print(f"dp size is {dp.shape}")
        for curIndex in range(0, numStep):  # 当前stone_pos的index
            for lastIndex in range(0, curIndex + 1):  # 上一次stone_pos的index
                curStone, lastStone = stones[curIndex], stones[lastIndex]
                action = curStone - lastStone  # 跳了多少
                # print(f"curStone,lastStone is {curStone},{lastStone}")
                if dp[curIndex][lastIndex]:
                    # 看看 curStone+action+(-1/0/1) 是否是有效的位置，有效再更新
                    #* 正如 想法2 里面所说,O(10^9)会超时。但是发现如果稍微降一点数量级上的复杂度，也就是在这里尽量减少搜索的范围，虽然还是O(10^9)，但就不会超时了。量变还是能引起点质变2333
                    after_stones = stones[curIndex:]
                    if curStone + action in after_stones:
                        # print(f"update dp[{stones.index(curStone +action)}][{curIndex}]")
                        dp[stones.index(curStone + action)][curIndex] = True
                    if curStone + action + 1 in after_stones:
                        # print(f"update dp[{stones.index(curStone +action+1)}][{curIndex}]")
                        dp[stones.index(curStone + action +
                                        1)][curIndex] = True
                    if curStone + action - 1 in after_stones and action - 1:
                        # print(f"update dp[{stones.index(curStone +action-1)}][{curIndex}]")
                        dp[stones.index(curStone + action -
                                        1)][curIndex] = True

        return any(dp[numStep - 1])


# 还有一种思路，https://blog.csdn.net/da_kao_la/article/details/105176065，其实还是