# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]level traverse from top to bottom
'''

from typing import Dict, List
from util import *

# 这不就是个BFS么...

##############################
### 大佬简洁的iterative ####
##############################
class Solution:
    """
    >>> sol = Solution()
    >>> sol.levelOrder([])
    []
    >>> sol.levelOrder(s)
    [[3], [4, 5], [1, 2]]
    >>> sol.levelOrder(t)
    [[4], [1, 2]]
    """
    def levelOrder(self, root: TreeNode) :#-> List[List[int]]:
        res = []
        cur_lev_node = [ root ] if root else []
        while len(cur_lev_node):
            res.append([ node.val for node in cur_lev_node ] )
            LRpair = [(node.left, node.right) for node in cur_lev_node]
            #* 外层循环先写，然后再是内层循环
            #* 这里很容易把 if leaf 漏掉... 然后就会报错val为None
            cur_lev_node = [leaf for LR in LRpair for leaf in LR if leaf ] 
        return res


##############################
### 自己臃肿的iterative #### 没有发挥python的优势啊..
##############################
    def levelOrder(self, root: TreeNode) :#-> List[List[int]]:
        levs_node, res = [], []
        if not root:
            return res

        levs_node.append([root])
        levIndex = 0

        while levIndex < len(levs_node):
            new_lev_node = []
            for node in levs_node[levIndex]:
                if (node.left):
                    new_lev_node.append(node.left)
                if (node.right):
                    new_lev_node.append(node.right)

            if len(new_lev_node):
                levs_node.append(new_lev_node)

            levIndex += 1
        
        res = []
        for lev in levs_node:
            new_lev =[]
            for node in lev:
                new_lev.append(node.val)
            
            res.append(new_lev)
                
        # return map(lambda lev: (lambda node: node.val,lev ) , levs_node)
        # res = map(lambda lev: (lambda node: node.val, lev), levs_node)
        # for i in res:
        #     for y in i:
        #         print(i,end=' ')
        # print(res)
        return res