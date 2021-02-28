<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard] [dp series]
'''

from typing import Dict, List
from util import *

import numpy as np
"""
#* Version1 :orginal Out of Time Limit version
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        numStep = len(stones)
        dp = np.array([[False] * numStep
                       for _ in range(numStep)])  # 目前是step的位置，上一步跳了action
        dp[0, 0] = True
            for curIndex in range(0, numStep):  # 当前stone_pos的index
            for lastIndex in range(0, curIndex + 1):  # 上一次stone_pos的index
                curStone, lastStone = stones[curIndex], stones[lastIndex]
                action = curStone - lastStone  # 跳了多少
                if dp[curIndex][lastIndex]:
                    # 看看 curStone+action+(-1/0/1) 是否是有效的位置，有效再更新
                    #* 正如 想法2 里面所说,O(10^9)会超时。但是发现如果稍微降一点数量级上的复杂度，也就是在这里尽量减少搜索的范围，虽然还是O(10^9)，但就不会超时了。量变还是能引起点质变2333
                    after_stones = stones[curIndex:]
                    if curStone + action in after_stones:
                        dp[stones.index(curStone + action)][curIndex] = True
                    if curStone + action + 1 in after_stones:
                        dp[stones.index(curStone + action +
                                        1)][curIndex] = True
                    if curStone + action - 1 in after_stones and action - 1:
                        dp[stones.index(curStone + action -
                                        1)][curIndex] = True

        return any(dp[numStep - 1])

#* Version 2： use dict to speed up . 内存稍稍改进 ， 速度从9000多ms降低到4000多ms ，beat 5.03% to 5.28%... 虽然version2和version3都是O(n^2)，但是version3会剪掉很多不必要的枝桠...不能小看常数集！
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        numStep = len(stones)
        stoneDict =dict({ stones[i]:i for i in range(len(stones)) } ) # 使用hashMap降低搜索速度
        dp = np.array([[False] * numStep
                       for _ in range(numStep)])  # 目前是step的位置，上一步跳了action
        dp[0, 0] = True
        for curIndex in range(0, numStep):  # 当前stone_pos的index
            for lastIndex in range(0, curIndex + 1):  # 上一次stone_pos的index
                curStone, lastStone = stones[curIndex], stones[lastIndex]
                action = curStone - lastStone  # 跳了多少
                if dp[curIndex][lastIndex]:
                    # 看看 curStone+action+(-1/0/1) 是否是有效的位置，有效再更新
                    tmp = stoneDict.get(curStone + action)
                    if tmp:    # if curStone + action in after_stones:
                        dp[tmp][curIndex] = True
                    tmp = stoneDict.get(curStone + action+1)
                    if tmp:
                        dp[tmp][curIndex] = True
                    tmp = stoneDict.get(curStone + action-1)
                    if action-1 and tmp :
                        dp[tmp][curIndex] = True

        return any(dp[numStep - 1])

#* Version 3 : 相比于version2，只走走得通的路
class Solution:
    def canCross(self, stones):
        import collections
        dic = collections.defaultdict(set)
        dic[0].add(0)
        for i in range(len(stones)):
            if stones[i] in dic:
                for val in dic[stones[i]]:
                    if val > 0:
                        dic[stones[i]+val].add(val)
                    if val > 1:
                        dic[stones[i]+val-1].add(val-1)
                    dic[stones[i]+val+1].add(val+1)
        return stones[-1] in dic

#* Version 4 : Version3的进一步代码上的精简，只走走得通的路，且只存有效的stone_pos的信息。但后者其实只是减少了内存开销，遍历的开销没有下下去，且还多了一些控制，所以速度稍微慢了一点，由version3的70%降低到只beat %60
"""
class Solution:
    def canCross(self, stones):
        """
        >>> s = Solution()
        >>> s.canCross([0,1,3,5,6,8,12,17])
        True
        >>> s.canCross([0,1,2,3,4,8,9,11])
        False
        """
        if stones[1] != 1:
            return False
        d = {x: set() for x in stones}
        d[1].add(1)
        for x in stones[:-1]:
            for j in d[x]:
                for k in range(j-1, j+2):       # py3中range 和 xrange结合起来了，which means range也是一个生成器而非直接返回一个数组了
                    if k > 0 and x+k in d:
                        d[x+k].add(k)
=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard] [dp series]
'''

from typing import Dict, List
from util import *

import numpy as np
"""
#* Version1 :orginal Out of Time Limit version
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        numStep = len(stones)
        dp = np.array([[False] * numStep
                       for _ in range(numStep)])  # 目前是step的位置，上一步跳了action
        dp[0, 0] = True
            for curIndex in range(0, numStep):  # 当前stone_pos的index
            for lastIndex in range(0, curIndex + 1):  # 上一次stone_pos的index
                curStone, lastStone = stones[curIndex], stones[lastIndex]
                action = curStone - lastStone  # 跳了多少
                if dp[curIndex][lastIndex]:
                    # 看看 curStone+action+(-1/0/1) 是否是有效的位置，有效再更新
                    #* 正如 想法2 里面所说,O(10^9)会超时。但是发现如果稍微降一点数量级上的复杂度，也就是在这里尽量减少搜索的范围，虽然还是O(10^9)，但就不会超时了。量变还是能引起点质变2333
                    after_stones = stones[curIndex:]
                    if curStone + action in after_stones:
                        dp[stones.index(curStone + action)][curIndex] = True
                    if curStone + action + 1 in after_stones:
                        dp[stones.index(curStone + action +
                                        1)][curIndex] = True
                    if curStone + action - 1 in after_stones and action - 1:
                        dp[stones.index(curStone + action -
                                        1)][curIndex] = True

        return any(dp[numStep - 1])

#* Version 2： use dict to speed up . 内存稍稍改进 ， 速度从9000多ms降低到4000多ms ，beat 5.03% to 5.28%... 虽然version2和version3都是O(n^2)，但是version3会剪掉很多不必要的枝桠...不能小看常数集！
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        numStep = len(stones)
        stoneDict =dict({ stones[i]:i for i in range(len(stones)) } ) # 使用hashMap降低搜索速度
        dp = np.array([[False] * numStep
                       for _ in range(numStep)])  # 目前是step的位置，上一步跳了action
        dp[0, 0] = True
        for curIndex in range(0, numStep):  # 当前stone_pos的index
            for lastIndex in range(0, curIndex + 1):  # 上一次stone_pos的index
                curStone, lastStone = stones[curIndex], stones[lastIndex]
                action = curStone - lastStone  # 跳了多少
                if dp[curIndex][lastIndex]:
                    # 看看 curStone+action+(-1/0/1) 是否是有效的位置，有效再更新
                    tmp = stoneDict.get(curStone + action)
                    if tmp:    # if curStone + action in after_stones:
                        dp[tmp][curIndex] = True
                    tmp = stoneDict.get(curStone + action+1)
                    if tmp:
                        dp[tmp][curIndex] = True
                    tmp = stoneDict.get(curStone + action-1)
                    if action-1 and tmp :
                        dp[tmp][curIndex] = True

        return any(dp[numStep - 1])

#* Version 3 : 相比于version2，只走走得通的路
class Solution:
    def canCross(self, stones):
        import collections
        dic = collections.defaultdict(set)
        dic[0].add(0)
        for i in range(len(stones)):
            if stones[i] in dic:
                for val in dic[stones[i]]:
                    if val > 0:
                        dic[stones[i]+val].add(val)
                    if val > 1:
                        dic[stones[i]+val-1].add(val-1)
                    dic[stones[i]+val+1].add(val+1)
        return stones[-1] in dic

#* Version 4 : Version3的进一步代码上的精简，只走走得通的路，且只存有效的stone_pos的信息。但后者其实只是减少了内存开销，遍历的开销没有下下去，且还多了一些控制，所以速度稍微慢了一点，由version3的70%降低到只beat %60
"""
class Solution:
    def canCross(self, stones):
        """
        >>> s = Solution()
        >>> s.canCross([0,1,3,5,6,8,12,17])
        True
        >>> s.canCross([0,1,2,3,4,8,9,11])
        False
        """
        if stones[1] != 1:
            return False
        d = {x: set() for x in stones}
        d[1].add(1)
        for x in stones[:-1]:
            for j in d[x]:
                for k in range(j-1, j+2):       # py3中range 和 xrange结合起来了，which means range也是一个生成器而非直接返回一个数组了
                    if k > 0 and x+k in d:
                        d[x+k].add(k)
>>>>>>> hesy/master
        return bool(d[stones[-1]])