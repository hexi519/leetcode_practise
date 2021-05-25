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


class StockSpanner:
    def __init__(self):
        from collections import deque
        self._mq = deque()
        self._index = 0

    def next(self, price: int) -> int:
        while len(self._mq) and price >= self._mq[-1][1]:
            self._mq.pop()
        self._index += 1
        ans = self._index - self._mq[-1][0] if len(self._mq)  else self._index
        
        self._mq.append((self._index, price))

        return ans


# Your StockSpanner object will be instantiated and called as such:

if __name__ == "__main__":
    obj = StockSpanner()
    # print(obj.next(100))
    # print(obj.next(80))
    # print(obj.next(60))
    # print(obj.next(70))
    print(obj.next(31))
    print(obj.next(41))
    print(obj.next(59))
    print(obj.next(70))