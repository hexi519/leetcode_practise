# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium] bs
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()


def getTime(k, piles):
    cnt = 0
    for pile in piles:
        cnt += pile // k + (1 if pile % k else 0)

    return cnt


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowerSpeed = max(sum(piles) // h, 1)  # lower bound -- fast time
        upperSpeed = max(piles)

        l, r = max(lowerSpeed, 1), upperSpeed + 1
        while l < r:
            mid = l + (r - l) // 2
            midTime = getTime(mid, piles)

            if midTime > h:  # advance speed
                l = mid + 1

            else:
                r = mid

        return l


if __name__ == "__main__":
    sol = Solution()
    piles, h = [3, 6, 7, 11], 8
    print(f"res is {sol.minEatingSpeed(piles,h)}")  # 4
    piles, h = [30, 11, 23, 4, 20], 5
    print(f"res is {sol.minEatingSpeed(piles,h)}")  # 30
    piles, h = [30, 11, 23, 4, 20], 6
    print(f"res is {sol.minEatingSpeed(piles,h)}")  # 23
    piles, h = [123], 124
    print(f"res is {sol.minEatingSpeed(piles,h)}")  # 1
