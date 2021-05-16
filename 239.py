# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard] monotonic queue
'''

from typing import Dict, List
from util import *
from loguru import logger as log

# ipdb.set_trace=blockIpdb
blockPrint()
# enablePrint()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        >>> s = Solution()
        >>> s.maxSlidingWindow([1],1)
        [1]
        """
        """
        # >>> s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
        # [3, 3, 5, 5, 6, 7]
        # >>> s.maxSlidingWindow([5,4,2,1],3)
        # [5, 4]
        # >>> s.maxSlidingWindow([5,4,2,1],4)
        # [5]
        # >>> s.maxSlidingWindow([1,3,1,2,0,5],3)
        # [3, 3, 2, 5]
        # >>> s.maxSlidingWindow([7,2,4],2)
        # [7, 4]
        # >>> s.maxSlidingWindow([3,2,1,0,-2],2)
        # [3, 2, 1, 0]
        """
        from collections import deque
        lenArr = len(nums)
        if lenArr < k:
            return [max(nums)]

        mq = deque([0])
        ans = []
        for curIndex in range(1, lenArr):
            # log.info(f"curIndex is {curIndex}({nums[curIndex]})")
            while len(mq) and nums[mq[-1]] <= nums[curIndex]:  # TODO 这里 等于也是没有意义的
                # log.info(f"mq[-1] is {mq[-1]}")
                mq.pop()
            mq.append(curIndex)

            # log.info(f"after pop, mq is {mq}")

            if curIndex >= k-1:  # 吐出来一个
                largestIndex = mq[0]
                while largestIndex < curIndex-k:
                    # ans.append(mq[0])
                    # log.info(f"mq[0] is {mq[-1]}")
                    mq.popleft()  # 会不会为空 --> 不可能
                    largestIndex = mq[0]
                ans.append(nums[largestIndex])

        return ans
