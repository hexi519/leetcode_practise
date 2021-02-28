<<<<<<< HEAD
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *

class Solution:
    """
    >>> sol = Solution()
    >>> sol.zigzagLevelOrder([])
    []
    >>> sol.zigzagLevelOrder(s)
    [[3], [5, 4], [1, 2]]
    >>> sol.zigzagLevelOrder(t)
    [[4], [2, 1]]
    """
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        cur_level_node = ([root], 1) if root else ([],1)
        res = []
        while len(cur_level_node[0]):
            # left->right (even) and right->left(odd)
            last_lev = cur_level_node[1]
            cur_res = [node.val
                       for node in cur_level_node[0]] if last_lev % 2 else [
                           node.val for node in cur_level_node[0][::-1]
                       ]
            res.append(cur_res)

            cur_level_node = ([
                node for par in cur_level_node[0]
                for node in (par.left, par.right) if node
            ], last_lev + 1)
        
        return res
=======
# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [medium]
'''

from typing import Dict, List
from util import *

class Solution:
    """
    >>> sol = Solution()
    >>> sol.zigzagLevelOrder([])
    []
    >>> sol.zigzagLevelOrder(s)
    [[3], [5, 4], [1, 2]]
    >>> sol.zigzagLevelOrder(t)
    [[4], [2, 1]]
    """
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        cur_level_node = ([root], 1) if root else ([],1)
        res = []
        while len(cur_level_node[0]):
            # left->right (even) and right->left(odd)
            last_lev = cur_level_node[1]
            cur_res = [node.val
                       for node in cur_level_node[0]] if last_lev % 2 else [
                           node.val for node in cur_level_node[0][::-1]
                       ]
            res.append(cur_res)

            cur_level_node = ([
                node for par in cur_level_node[0]
                for node in (par.left, par.right) if node
            ], last_lev + 1)
        
        return res
>>>>>>> hesy/master
