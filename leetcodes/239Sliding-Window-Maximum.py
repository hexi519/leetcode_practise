# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard] monotonic queue
'''

from typing import Dict, List
from util import *
from loguru import logger as log

# import ipdb
# ipdb.set_trace=blockIpdb

def blockPrint():
    sys.stdout = open(os.devnull, 'w')
blockPrint()
# enablePrint()

class MononicQueue:
    def __init__(self, k, nums):
        self._size = k
        self._arr = nums

        from collections import deque
        # self._mq = deque(maxlen=self._size)  # TODO 如果超过了size怎么办.self...
        self._mq = deque()  # TODO 如果超过了size怎么办.self...  
        #! 不用考虑size的事情

    def push_back(self, idx):
        # if self._size<=len(self._mq):   # TODO 不用考虑超过的事情...
        #     print(f"\tpop due to overflow of the stack")
        #     self._mq.popleft()
        # TODO deque如何实现的  继承queue？ from list? 可以有len（）? 感觉用的不是很熟啊...
        # ipdb.set_trace()
        while len(self._mq) and self._arr[idx] >= self._arr[self._mq[-1]]:
            self._mq.pop()
        # if num < self._mq[0]:  # TODO deque是可以遍历的吧... 既可以直接看左边，又可以直接看右边？其实stack也是哈...

        # * 确保是个单调递减的队列
        print(f"\tpush back {self._arr[idx]}")
        self._mq.append(idx)

    def popleft(self):
        print(f"\tpop left of mq and to be {self._mq}")
        return self._mq.popleft()

    def __str__(self):
        return f"deque is {list(map(lambda x : self._arr[x], self._mq))}"

    def getLargest(self):
        print(f"\tin getLargest, self._mq is {self._mq}")
        # return self._mq[0]
        try:
            return self._mq[0]
            # return len(self._arr)-1
        except IndexError:
            # ipdb.set_trace()
            print(f"\t Error: len of self._mq is {len(self._mq)}")
            print(f"\t Error: self._mq is {self.__str__()}")
            # exit(-1)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        >>> s = Solution()
        >>> s.maxSlidingWindow([5,4,2,1],3)
        [5, 4]
        >>> s.maxSlidingWindow([5,4,2,1],4)
        [5]
        """
        """
        #>>> s.maxSlidingWindow([1,3,1,2,0,5],3)
        #[3, 3, 2, 5]
        #>>> s.maxSlidingWindow([7,2,4],2)
        #[7, 4]
        #>>> s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
        #[3, 3, 5, 5, 6, 7]
        #>>> s.maxSlidingWindow([3,2,1,0,-2],2)
        #[3, 2, 1, 0]
        #>>> s.maxSlidingWindow([1],1)
        #[1]
        """
        ans = []
        arrLen = len(nums)
        curIdx = 0
        mq = MononicQueue(k,nums)
        if k < arrLen:
            for curIdx in range(k):
                mq.push_back(curIdx)
                print(mq)

            print(f'done before k')
            ans.append(nums[mq.getLargest()])
            for curIdx in range(k,arrLen):  # pop这么多次
                mq.push_back(curIdx)
                largestIdx = mq.getLargest()
                print(f"\t curIdx is {curIdx}({nums[curIdx]})(curIdx-k is {curIdx-k}), and largestIdx is {largestIdx}({nums[largestIdx]})")
                while largestIdx <= curIdx-k:
                    mq.popleft()
                    largestIdx = mq.getLargest()
                
                ans.append( nums[largestIdx] )
                print(mq)

        else:
            return [max(nums)]

        return ans


# s = Solution()
# s.maxSlidingWindow([1,3,1,2,0,5],3)