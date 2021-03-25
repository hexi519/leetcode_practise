# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''
from loguru import logger
from typing import Dict, List
from util import *

#* union find
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        >>> s= Solution()
        >>> s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
        2
        >>> s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
        3
        >>> s.findCircleNum([])
        0
        >>> s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
        1
        >>> s.findCircleNum([[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
        8
        """
        cityNum = len(isConnected)
        if cityNum == 0: return 0
        numP = 0
        self.par = [city for city in range(cityNum)]
        self.rank = [0 for city in range(cityNum)]  #! 有了秩优化还是会快一些的（现在数据集还不算大，大了以后就比较明显）

        for fromNode in range(cityNum):
            for toNode in range(fromNode+1,cityNum):
                if isConnected[fromNode][toNode]:
                    self.union(fromNode, toNode)

        for node in range(cityNum):
            numP += 1 if self.par[node] == node else 0
        return numP

    def union(self, fromNode, toNode):
        # if fromNode == toNode: return     # avoid when calling
        fromPar, toPar = self.findPar(fromNode), self.findPar(toNode)
        if fromPar != toPar:
            if self.rank[fromPar] < self.rank[toPar]:
                self.par[fromPar] = self.par[toPar]     # TODO 要注意的的点(一开始写错了) 是修改根节点的父节点和秩，而不是修改当前节点！union中只修改根节点，find路径压缩的时候才修改当前节点
                self.rank[fromPar] += 1
            else:
                self.par[toPar] = self.par[fromPar]
                self.rank[toNode] += 1

    def findPar(self, node):
        if self.par[node] == node: return node
        self.par[node] = self.findPar(self.par[node])
        return self.par[node]

#* dfs
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        >>> s= Solution()
        >>> s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
        2
        >>> s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
        3
        >>> s.findCircleNum([])
        0
        >>> s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
        1
        >>> s.findCircleNum([[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
        8
        """
        self.cityNum = len(isConnected)
        self.visited = [False for node in range(self.cityNum)]
        self.count=0
        self.isConnected = isConnected
        # 遍历每一条边，如果有连接，dfs
        for fromNode in range(self.cityNum):
            # self.dfs( formNode,toNode )     # TODO 这样写就思路没有清晰，dfs在这题里面不应该从一条边开始，而是应该从一个点开始
            if not self.visited[fromNode]: 
                self.count+=1
                self.visited[fromNode]=True
            self.dfs_recursive(fromNode)
        return self.count

    def dfs_recursive(self, fromNode):
        for toNode in range(self.cityNum):
            if self.isConnected[fromNode][toNode] and not self.visited[toNode] :  # 连接着 且 还没被着色过(还需要遍历)
                self.visited[toNode]=True
                self.dfs(toNode)
