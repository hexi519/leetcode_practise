# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]level traverse from top to bottom 第二次刷成功了
'''

from typing import Dict, List
from util import *
from loguru import logger as log


# 这不就是个BFS么...

##############################
### 大佬简洁的iterative ####
##############################


class Solution:
    # bfs
    def levelOrder(self, root: TreeNode):  # -> List[List[int]]:
        """
        >>> sol = Solution()
        >>> sol.levelOrder(None)
        []
        >>> sol.levelOrder(s)
        [[3], [4, 5], [1, 2]]
        >>> sol.levelOrder(t)
        [[4], [1, 2]]
        """
        curLev, ans = [root], []
        if root is None : return []

        def help_dfs( curLev ):
            if not len(curLev) : return

            nonlocal ans
            ans.append( [ node.val for node in curLev ] )
            tmp = [ [node.left,node.right] for node in curLev] 
            curLev = [ node for nodePair in tmp for node in nodePair if node ]
            help_dfs(curLev)

        help_dfs(curLev)

        return ans

"""
    def levelOrder(self, root: TreeNode):  # -> List[List[int]]:
        res = []
        cur_lev_node = [root] if root else []
        while len(cur_lev_node):
            res.append([node.val for node in cur_lev_node])
            LRpair = [(node.left, node.right) for node in cur_lev_node] # 这里写成[node.left, node.right]也没关系
            # * 外层循环先写，然后再是内层循环
            # * 这里很容易把 if leaf 漏掉... 然后就会报错val为None
            cur_lev_node = [leaf for LR in LRpair for leaf in LR if leaf]
        return res

"""
