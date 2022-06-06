# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *
from loguru import logger as log

#ipdb.set_trace=blockIpdb

blockPrint()
enablePrint()

from collections import deque, defaultdict


class Solution:
    res = 0

    def minJumps(self, arr: List[int]) -> int:
        if len(arr) < 2: return 0

        idxs = deque([0])
        visited = [False for _ in range(len(arr))]
        visited[0] = True

        hashMap = defaultdict(list)
        for i in range(len(arr)):
            hashMap[arr[i]].append(i)

        self.BFS(visited, hashMap, 1, idxs, arr)

        return self.res

    def BFS(self, visited, hashMap, step, idxs, arr):
        newIdxs = deque()
        while len(idxs):
            curIdx = idxs.popleft()

            for nextIdx in [curIdx + 1, curIdx - 1]:
                if 0 <= nextIdx < len(arr) and not visited[nextIdx]:
                    if nextIdx == len(arr) - 1:
                        self.res = step
                        return
                    newIdxs.append(nextIdx)
                    visited[nextIdx] = True

            for nextIdx in hashMap[arr[curIdx]]:
                if not visited[nextIdx]:
                    if nextIdx == len(arr) - 1:
                        self.res = step
                        return

                    newIdxs.append(nextIdx)
                    visited[nextIdx] = True

            hashMap[arr[curIdx]] = []  #* important for o(n^2)'s bad case

        self.BFS(visited, hashMap, step + 1, newIdxs, arr)


if __name__ == "__main__":
    sol = Solution()
    print(f"res is {sol.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404])}")  # 3
    print(f"res is {sol.minJumps([0,1,2,3])}")  # 3
    print(f"res is {sol.minJumps([0,1,0,3])}")  # 2
    print(f"res is {sol.minJumps([7,6,9,6,9,6,9,7])}")  # 1
    print(f"res is {sol.minJumps([7])}")  # 0
