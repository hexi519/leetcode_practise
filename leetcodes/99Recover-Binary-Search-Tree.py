# -*- encoding: utf-8 -*-
'''
@Author  :   hesy 
@Contact :   hesy519@gmail.com
@Desc    :   [hard]
'''

from typing import Dict, List
from util import *
from loguru import logger as log


class Solution:
    # with O(n) space
    """
    def recoverTree(self, root: TreeNode) -> None:
        # 先找出其中序遍历
        nodeStack, inorder, cur = [], [], root
        nodes = []
        while len(nodeStack) or cur:
            if cur:
                nodeStack.append(cur)
                cur = cur.left
            else:
                cur = nodeStack.pop()
                inorder.append(cur.val)
                nodes.append(cur)       # 还得把节点的引用也记下来...
                cur = cur.right

        times, flag = [0, 0], 0
        for idx, number in enumerate(inorder):
            if idx == 0:
                continue
            if number < inorder[idx-1]:
                times[flag] = idx if flag else idx-1  # 第一次记录大的 (前面的)
                flag += 1

        if flag == 1:
            nodes[times[0]].val, nodes[times[0] +
                                       1].val = nodes[times[0]+1].val, nodes[times[0]].val

        if flag == 2:
            nodes[times[0]].val, nodes[times[1]
                                       ].val = nodes[times[1]].val, nodes[times[0]].val
    """

    # morris traversial, with O(1) space
    def recoverTree(self, root: TreeNode) -> None:
        """
        >>> s = Solution()
        >>> s.recoverTree(tt)
        [3, 4, 5]
        >>> s.recoverTree(None)
        []
        """
        nodePairs = [0, 0]   # for record nodes
        flag = 0
        # inorder traversial with morris
        cur, pre = root, None
        while cur:
            # 对于每个点， 找其左边的最右子节点 ，没有的话建立
            mor = cur.left
            if mor:
                while mor.right and mor.right != cur:
                    mor = mor.right

                if mor.right == cur:  # 右移动
                    if pre and pre.val > cur.val:
                        nodePairs[flag] = (pre, cur)
                        flag += 1
                    
                    mor.right = None
                    pre, cur = cur, cur.right

                elif not mor.right:   # 左移动
                    mor.right, cur = cur, cur.left

            else:
                if pre and pre.val > cur.val:
                    nodePairs[flag] = (pre, cur)
                    flag += 1    
                pre, cur = cur, cur.right

        if flag == 1:
            pre, cur = nodePairs[0]
            pre.val, cur.val = cur.val, pre.val

        if flag == 2:
            pre, cur = nodePairs[0][0], nodePairs[1][1]
            pre.val, cur.val = cur.val, pre.val
