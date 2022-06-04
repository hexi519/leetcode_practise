# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


def valid(idx, length):
    return idx >= 0 and idx < length


class Solution:
    def canReach(self, A, i):
        visited = [False for _ in range(len(A))]
        from collections import deque
        queue = deque([i])

        while len(queue):
            curIdx = queue.popleft()
            visited[curIdx] = True
            if A[curIdx] == 0:
                return True

            leftIdx, rightIdx = curIdx - A[curIdx], curIdx + A[curIdx]
            if valid(leftIdx, len(A)) and not visited[leftIdx]:
                queue.append(leftIdx)

            if valid(rightIdx, len(A)) and not visited[rightIdx]:
                queue.append(rightIdx)

        # print(f"visited is {visited}")
        return False


if __name__ == '__main__':
    sol = Solution()
    print(f"res is {sol.canReach([4, 2, 3, 0, 3, 1, 2], 5)}")  # true
    print(f"res is {sol.canReach([4,2,3,0,3,1,2], 0)}")  # true
    print(f"res is {sol.canReach([4,1,3], 1)}")  # False
